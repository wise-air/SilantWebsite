from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from rest_framework import serializers, generics, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .filters import *
from .forms import *
from .models import *
from .templatetags.silant_filters import user_role, _role as get_role

default_paginate_by = 5


class MainPage(TemplateView):
    template_name = 'default.html'


class ContextMixin:
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user_role'] = get_role(self.request.user)
        data['meta'] = self.model._meta
        return data


class ManagerMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if get_role(request.user) == 'MANAGER':
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class ManagerServiceMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        item = self.get_object()
        user = request.user
        match get_role(user):
            case 'MANAGER':
                return super().dispatch(request, *args, **kwargs)
            case 'SERVICE' if user.silantpermissions.service_firm == item.service_firm:
                return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class ManagerClientServiceMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        item = self.get_object()
        user = request.user
        match get_role(user):
            case 'MANAGER':
                return super().dispatch(request, *args, **kwargs)
            case 'CLIENT' if user.silantpermissions.client == item.vehicle.client:
                return super().dispatch(request, *args, **kwargs)
            case 'SERVICE' if user.silantpermissions.service_firm == item.service_firm:
                return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class VocListView(ContextMixin, LoginRequiredMixin, ListView):
    context_object_name = 'items'
    template_name = 'silant/voc_list.html'
    paginate_by = default_paginate_by


class VocDetailView(ContextMixin, DetailView):
    template_name = 'silant/voc_item.html'


class VocAddView(ContextMixin, ManagerMixin, CreateView):
    template_name = 'silant/voc_edit.html'


class VocUpdateView(ContextMixin, ManagerMixin, UpdateView):
    template_name = 'silant/voc_edit.html'


class VocDeleteView(ContextMixin, ManagerMixin, DeleteView):
    template_name = 'silant/voc_delete.html'


#######################################################

class ClientListView(VocListView):
    model = Client


class ClientDetailView(VocDetailView):
    model = Client


class ClientAddView(VocAddView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('silant.client.list')


class ClientUpdateView(VocUpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('silant.client.list')


class ClientDeleteView(VocDeleteView):
    model = Client
    success_url = reverse_lazy('silant.client.list')


#######################################################
class TechTypeListView(VocListView):
    model = TechType


class TechTypeDetailView(VocDetailView):
    model = TechType


class TechTypeAddView(VocAddView):
    model = TechType
    form_class = TechTypeForm
    success_url = reverse_lazy('silant.tech_type.list')


class TechTypeUpdateView(VocUpdateView):
    model = TechType
    form_class = TechTypeForm
    success_url = reverse_lazy('silant.tech_type.list')


class TechTypeDeleteView(VocDeleteView):
    model = TechType
    success_url = reverse_lazy('silant.tech_type.list')


#######################################################
class EngineTypeListView(VocListView):
    model = EngineType


class EngineTypeDetailView(VocDetailView):
    model = EngineType


class EngineTypeAddView(VocAddView):
    model = EngineType
    form_class = EngineTypeForm
    success_url = reverse_lazy('silant.engine_type.list')


class EngineTypeUpdateView(VocUpdateView):
    model = EngineType
    form_class = EngineTypeForm
    success_url = reverse_lazy('silant.engine_type.list')


class EngineTypeDeleteView(VocDeleteView):
    model = EngineType
    success_url = reverse_lazy('silant.engine_type.list')


#######################################################
class GearTypeListView(VocListView):
    model = GearType


class GearTypeDetailView(VocDetailView):
    model = GearType


class GearTypeAddView(VocAddView):
    model = GearType
    form_class = GearTypeForm
    success_url = reverse_lazy('silant.gear_type.list')


class GearTypeUpdateView(VocUpdateView):
    model = GearType
    form_class = GearTypeForm
    success_url = reverse_lazy('silant.gear_type.list')


class GearTypeDeleteView(VocDeleteView):
    model = GearType
    success_url = reverse_lazy('silant.gear_type.list')


#######################################################
class DriveAxelTypeListView(VocListView):
    model = DriveAxelType


class DriveAxelTypeDetailView(VocDetailView):
    model = DriveAxelType


class DriveAxelTypeAddView(VocAddView):
    model = DriveAxelType
    form_class = DriveAxelTypeForm
    success_url = reverse_lazy('silant.drive_axel_type.list')


class DriveAxelTypeUpdateView(VocUpdateView):
    model = DriveAxelType
    form_class = DriveAxelTypeForm
    success_url = reverse_lazy('silant.drive_axel_type.list')


class DriveAxelTypeDeleteView(VocDeleteView):
    model = DriveAxelType
    success_url = reverse_lazy('silant.drive_axel_type.list')


#######################################################
class SteerAxelTypeListView(VocListView):
    model = SteerAxelType


class SteerAxelTypeDetailView(VocDetailView):
    model = SteerAxelType


class SteerAxelTypeAddView(VocAddView):
    model = SteerAxelType
    form_class = SteerAxelTypeForm
    success_url = reverse_lazy('silant.steer_axel_type.list')


class SteerAxelTypeUpdateView(VocUpdateView):
    model = SteerAxelType
    form_class = SteerAxelTypeForm
    success_url = reverse_lazy('silant.steer_axel_type.list')


class SteerAxelTypeDeleteView(VocDeleteView):
    model = SteerAxelType
    success_url = reverse_lazy('silant.steer_axel_type.list')


#######################################################
class ServiceFirmListView(VocListView):
    model = ServiceFirm


class ServiceFirmDetailView(LoginRequiredMixin, VocDetailView):
    model = ServiceFirm


class ServiceFirmAddView(VocAddView):
    model = ServiceFirm
    form_class = ServiceFirmForm
    success_url = reverse_lazy('silant.service_firm.list')


class ServiceFirmUpdateView(VocUpdateView):
    model = ServiceFirm
    form_class = ServiceFirmForm
    success_url = reverse_lazy('silant.service_firm.list')


class ServiceFirmDeleteView(VocDeleteView):
    model = ServiceFirm
    success_url = reverse_lazy('silant.service_firm.list')


#######################################################
class ServiceTypeListView(VocListView):
    model = ServiceType


class ServiceTypeDetailView(LoginRequiredMixin, VocDetailView):
    model = ServiceType


class ServiceTypeAddView(VocAddView):
    model = ServiceType
    form_class = ServiceTypeForm
    success_url = reverse_lazy('silant.service_type.list')


class ServiceTypeUpdateView(VocUpdateView):
    model = ServiceType
    form_class = ServiceTypeForm
    success_url = reverse_lazy('silant.service_type.list')


class ServiceTypeDeleteView(VocDeleteView):
    model = ServiceType
    success_url = reverse_lazy('silant.service_type.list')


#######################################################
class RepairMethodListView(VocListView):
    model = RepairMethod


class RepairMethodDetailView(LoginRequiredMixin, VocDetailView):
    model = RepairMethod


class RepairMethodAddView(VocAddView):
    model = RepairMethod
    form_class = RepairMethodForm
    success_url = reverse_lazy('silant.repair_method.list')


class RepairMethodUpdateView(VocUpdateView):
    model = RepairMethod
    form_class = RepairMethodForm
    success_url = reverse_lazy('silant.repair_method.list')


class RepairMethodDeleteView(VocDeleteView):
    model = RepairMethod
    success_url = reverse_lazy('silant.repair_method.list')


#######################################################
class FailurePartListView(VocListView):
    model = FailurePart


class FailurePartDetailView(LoginRequiredMixin, VocDetailView):
    model = FailurePart


class FailurePartAddView(VocAddView):
    model = FailurePart
    form_class = RepairMethodForm
    success_url = reverse_lazy('silant.failure_part.list')


class FailurePartUpdateView(VocUpdateView):
    model = FailurePart
    form_class = RepairMethodForm
    success_url = reverse_lazy('silant.failure_part.list')


class FailurePartDeleteView(VocDeleteView):
    model = FailurePart
    success_url = reverse_lazy('silant.failure_part.list')


#######################################################
class VehicleListView(ListView):
    model = Vehicle
    context_object_name = 'items'
    template_name = 'silant/vehicle_list.html'
    ordering = 'shipping_date'
    paginate_by = default_paginate_by
    user_role = ''
    __field_list = None

    @classmethod
    def field_list(cls):
        if not cls.__field_list:
            fields = cls.model._meta.get_fields()
            cls.__field_list = [f.name for f in fields if f.__class__.__name__ not in ('ManyToOneRel', 'BigAutoField')]
        return cls.__field_list

    def dispatch(self, request, *args, **kwargs):
        self.user_role = get_role(request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(VehicleListView, self).get_queryset()

        ordering = self.ordering
        filter = self.request.GET.copy()
        for v in self.field_list():
            if f'order_{v}' in filter:
                ordering = f'{v}'
        self.ordering = ordering
        queryset = queryset.order_by(ordering)

        match self.user_role:
            case 'CLIENT':
                queryset = queryset.filter(client=self.request.user.silantpermissions.client)
            case 'SERVICE':
                queryset = queryset.filter(service_firm=self.request.user.silantpermissions.service_firm)
        self.filter_set = VehicleFilter(self.request.GET, queryset, request=self.request)
        return self.filter_set.qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user_role'] = self.user_role
        data['meta'] = self.model._meta
        data['filter_set'] = self.filter_set
        data['ordering'] = self.ordering
        return data


class VehicleDetailView(ContextMixin, AccessMixin, DetailView):
    model = Vehicle
    template_name = 'silant/vehicle_item.html'

    def dispatch(self, request, *args, **kwargs):
        item = self.get_object()
        match get_role(request.user):
            case 'MANAGER':
                return super().dispatch(request, *args, **kwargs)
            case 'CLIENT':
                if item.client == request.user.silantpermissions.client:
                    return super().dispatch(request, *args, **kwargs)
            case 'SERVICE':
                if item.service_firm == request.user.silantpermissions.service_firm:
                    return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class VehicleAddView(ContextMixin, ManagerMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'silant/vehicle_edit.html'
    success_url = reverse_lazy('silant.vehicle.list')


class VehicleUpdateView(ContextMixin, ManagerMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'silant/vehicle_edit.html'
    success_url = reverse_lazy('silant.vehicle.list')



class VehicleDeleteView(ContextMixin, ManagerMixin, DeleteView):
    model = Vehicle
    template_name = 'silant/vehicle_delete.html'
    success_url = reverse_lazy('silant.vehicle.list')


class HandBkListVehicleView(ListView):
    model = Vehicle
    context_object_name = 'handbk_vehicle'
    template_name = 'silant/vehicle_handbk.html'
    user_role = ''
    __field_list = None


#######################################################
class ServiceListView(AccessMixin, ListView):
    model = Service
    context_object_name = 'items'
    template_name = 'silant/service_list.html'
    ordering = 'date'
    paginate_by = 15
    user_role = ''
    __field_list = None
    @classmethod
    def field_list(cls):
        if not cls.__field_list:
            fields = cls.model._meta.get_fields()
            cls.__field_list = [f.name for f in fields if f.__class__.__name__ not in ('ManyToOneRel', 'BigAutoField')]
            cls.__field_list.remove('vehicle')
            cls.__field_list.append('vehicle__tech_type')
            cls.__field_list.append('vehicle__vehicle_number')
        return cls.__field_list

    def dispatch(self, request, *args, **kwargs):
        self.user_role = get_role(request.user)
        if not self.user_role:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(ServiceListView, self).get_queryset()

        ordering = self.ordering
        filter = self.request.GET.copy()
        for v in self.field_list():
            if f'order_{v}' in filter:
                ordering = f'{v}'
        self.ordering = ordering
        queryset = queryset.order_by(ordering)

        match self.user_role:
            case 'CLIENT':
                queryset = queryset.filter(vehicle__client=self.request.user.silantpermissions.client)
            case 'SERVICE':
                queryset = queryset.filter(service_firm=self.request.user.silantpermissions.service_firm)
        self.filter_set = ServiceFilter(self.request.GET, queryset, request=self.request)
        return self.filter_set.qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user_role'] = self.user_role
        data['meta'] = self.model._meta
        data['filter_set'] = self.filter_set
        data['ordering'] = self.ordering
        return data


class ServiceDetailView(ContextMixin, ManagerClientServiceMixin, DetailView):
    model = Service
    template_name = 'silant/service_item.html'


class ServiceAddView(ContextMixin, AccessMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'silant/service_edit.html'
    success_url = reverse_lazy('silant.service.list')

    def get_form_kwargs(self):
        kwargs = super(ServiceAddView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        if get_role(request.user) == '':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ServiceUpdateView(ContextMixin, ManagerClientServiceMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'silant/service_edit.html'
    success_url = reverse_lazy('silant.service.list')

    def get_form_kwargs(self):
        kwargs = super(ServiceUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ServiceDeleteView(ContextMixin, ManagerMixin, DeleteView):
    model = Service
    template_name = 'silant/service_delete.html'
    success_url = reverse_lazy('silant.service.list')


class HandBkListServiceView(ListView):
    model = Service
    context_object_name = 'handbk_service'
    template_name = 'silant/service_handbk.html'
    user_role = ''
    __field_list = None


#######################################################
class ClaimListView(AccessMixin, ListView):
    model = Claim
    context_object_name = 'items'
    template_name = 'silant/claim_list.html'
    ordering = 'failure_date'
    paginate_by = default_paginate_by
    user_role = ''
    __field_list = None
    @classmethod
    def field_list(cls):
        if not cls.__field_list:
            fields = cls.model._meta.get_fields()
            cls.__field_list = [f.name for f in fields if f.__class__.__name__ not in ('ManyToOneRel', 'BigAutoField')]
            cls.__field_list.remove('vehicle')
            cls.__field_list.append('vehicle__tech_type')
            cls.__field_list.append('vehicle__vehicle_number')
        return cls.__field_list

    def dispatch(self, request, *args, **kwargs):
        self.user_role = get_role(request.user)
        if not self.user_role:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(ClaimListView, self).get_queryset()

        ordering = self.ordering
        filter = self.request.GET.copy()
        for v in self.field_list():
            if f'order_{v}' in filter:
                ordering = f'{v}'
        self.ordering = ordering
        queryset = queryset.order_by(ordering)

        match self.user_role:
            case 'CLIENT':
                queryset = queryset.filter(vehicle__client=self.request.user.silantpermissions.client)
            case 'SERVICE':
                queryset = queryset.filter(service_firm=self.request.user.silantpermissions.service_firm)
        self.filter_set = ClimeFilter(self.request.GET, queryset, request=self.request)
        return self.filter_set.qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user_role'] = self.user_role
        data['meta'] = self.model._meta
        data['filter_set'] = self.filter_set
        data['ordering'] = self.ordering
        return data


class ClaimDetailView(ContextMixin, ManagerClientServiceMixin, DetailView):
    model = Claim
    template_name = 'silant/claim_item.html'


class ClaimAddView(ContextMixin, AccessMixin, CreateView):
    model = Claim
    form_class = ClaimForm
    template_name = 'silant/claim_edit.html'
    success_url = reverse_lazy('silant.claim.list')

    def get_form_kwargs(self):
        kwargs = super(ClaimAddView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        if get_role(request.user) in ('MANAGER', 'SERVICE'):
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class ClaimUpdateView(ContextMixin, ManagerServiceMixin, UpdateView):
    model = Claim
    form_class = ClaimForm
    template_name = 'silant/claim_edit.html'
    success_url = reverse_lazy('silant.claim.list')

    def get_form_kwargs(self):
        kwargs = super(ClaimUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ClaimDeleteView(ContextMixin, ManagerMixin, DeleteView):
    model = Claim
    template_name = 'silant/claim_delete.html'
    success_url = reverse_lazy('silant.claim.list')


class HandBkListClaimView(ListView):
    model = Claim
    context_object_name = 'handbk_claim'
    template_name = 'silant/claim_handbk.html'
    user_role = ''
    __field_list = None


#######################################################
class VehicleUnAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        depth = 2
        fields = [
            'id',
            'tech_type',
            'vehicle_number',
            'engine_type',
            'engine_number',
            'gear_type',
            'gear_number',
            'drive_axel_type',
            'drive_axel_number',
            'steer_axel_type',
            'steer_axel_number',
        ]


class VehicleAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        depth = 2
        fields = [
            'id',
            'tech_type',
            'vehicle_number',
            'engine_type',
            'engine_number',
            'gear_type',
            'gear_number',
            'drive_axel_type',
            'drive_axel_number',
            'steer_axel_type',
            'steer_axel_number',
            'contract',
            'shipping_date',
            'consumer',
            'address',
            'equipment',
            'client',
            'service_firm',
        ]


class VehicleListAPIView(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    user_role = ''

    def dispatch(self, request, *args, **kwargs):
        self.user_role = get_role(request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_serializer_class(self):
        return VehicleUnAuthSerializer if self.user_role == '' else VehicleAuthSerializer

    def get_queryset(self):
        queryset = super(VehicleListAPIView, self).get_queryset()
        match self.user_role:
            case 'CLIENT':
                queryset = queryset.filter(client=self.request.user.silantpermissions.client)
            case 'SERVICE':
                queryset = queryset.filter(service_firm=self.request.user.silantpermissions.service_firm)
        return queryset


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        depth = 2
        fields = [
            'id',
            'vehicle',
            'service_type',
            'date',
            'hours',
            'order_number',
            'order_date',
            'service_firm',
        ]


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        match get_role(self.request.user):
            case 'MANAGER':
                return Service.objects.all()
            case 'CLIENT':
                return Service.objects.filter(client=self.request.user.silantpermissions.client)
            case 'SERVICE':
                return Service.objects.filter(service_firm=self.request.user.silantpermissions.service_firm)
        return Service.objects.none()


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        depth = 2
        fields = [
            'id',
            'vehicle',
            'failure_date',
            'hours',
            'failure_part',
            'failure_type',
            'repair_method',
            'spare',
            'repaired_date',
            'service_firm',
        ]


class ClaimListAPIView(generics.ListAPIView):
    serializer_class = ClaimSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        match get_role(self.request.user):
            case 'MANAGER':
                return Service.objects.all()
            case 'CLIENT':
                return Service.objects.filter(vehicle__client=self.request.user.silantpermissions.client)
            case 'SERVICE':
                return Service.objects.filter(service_firm=self.request.user.silantpermissions.service_firm)
        return Service.objects.none()


