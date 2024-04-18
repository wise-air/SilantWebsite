import re

from django import template
from django.http import QueryDict
from django.urls import reverse

import silant

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()

@register.simple_tag(takes_context=True)
def vehicle_replace(context, **kwargs):
    return _order_replace(silant.views.VehicleListView, context, **kwargs)


@register.simple_tag(takes_context=True)
def service_replace(context, **kwargs):
    return _order_replace(silant.views.ServiceListView, context, **kwargs)


@register.simple_tag(takes_context=True)
def claim_replace(context, **kwargs):
    return _order_replace(silant.views.ClaimListView, context, **kwargs)


def _order_replace(view, context, **kwargs):
    remove = view.field_list()
    d = {k: v for k, v in context['request'].GET.items() if k[6:] not in remove}
    for k, v in kwargs.items():
        d[f'order_{k}'] = ''
    query_dict = QueryDict('', mutable=True)
    query_dict.update(d)
    return query_dict.urlencode()


@register.simple_tag(takes_context=True)
def reverse_url(context, middle, end):
    return f'silant.{camel_to_snake(middle)}.{end}'


@register.filter()
def camel_to_snake(value):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', value).lower()


@register.filter()
def days_string(value):
    if value % 100 in range(5, 19):
        return 'дней'
    if value % 10 == 1:
        return 'день'
    if value % 10 in range(2, 4):
        return 'дня'
    return 'дней'


@register.simple_tag(takes_context=True)
def create_link(context, item, link_type):
    if _role(context.request.user) == 'MANAGER':
        return reverse(f'silant.{link_type}.update', args=(item.pk,))
    return reverse(f'silant.{link_type}.detail', args=(item.pk,))


@register.simple_tag(takes_context=True)
def create_link_copy(context, item, link_type):
    user = context.request.user
    match _role(user):
        case "MANAGER":
            return reverse(f'silant.{link_type}.update', args=(item.pk,))
        case "CLIENT":
            if user.silantpermissions.client == item.client:
                return reverse(f'silant.{link_type}.detail', args=(item.pk,))
        case "SERVICE":
            if user.silantpermissions.service_firm == item.service_firm:
                return reverse(f'silant.{link_type}.detail', args=(item.pk,))
    return reverse(f'silant.{link_type}.detail', args=(item.pk,))


@register.simple_tag(takes_context=True)
def user_role(context):
    return _role(context.request.user)


@register.simple_tag(takes_context=True)
def can_add_vehicle(context, object_name):
    return _role(context.request.user) == 'MANAGER' and object_name == 'Vehicle'


@register.simple_tag(takes_context=True)
def can_add_service(context, object_name):
    return _role(context.request.user) in ['MANAGER', 'CLIENT', 'SERVICE'] and object_name == 'Service'


@register.simple_tag(takes_context=True)
def can_add_claim(context, object_name):
    return _role(context.request.user) in ['MANAGER', 'SERVICE'] and object_name == 'Claim'


def _role(user):
    if not user.is_authenticated:
        return ''
    if user.is_superuser:
        return 'MANAGER'
    try:
        return user.silantpermissions.role
    except Exception:
        return ''


