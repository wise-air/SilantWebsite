from allauth.account.forms import LoginForm as AuthLoginForm, PasswordField
from allauth.utils import get_username_max_length
from django import forms
from django.core.exceptions import ValidationError

from .models import *
from .templatetags.silant_filters import _role as get_role


class LoginForm(AuthLoginForm):
    password = PasswordField(label="Пароль", autocomplete="current-password")
    remember = forms.BooleanField(label="Запомнить меня", required=False)
    error_messages = {
        "account_inactive": "Этот аккаунт в данный момент заблокирован.",
        "email_password_mismatch":
            "The email address and/or password you specified are not correct."
        ,
        "username_password_mismatch":
            "Имя пользователя и/или пароль не правильные."
        ,
    }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        login_widget = forms.TextInput(
            attrs={"placeholder": "Имя пользователя", "autocomplete": "username"}
        )
        login_field = forms.CharField(
            label="Имя пользователя",
            widget=login_widget,
            max_length=get_username_max_length(),
        )
        self.fields["login"] = login_field


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'descr']


class TechTypeForm(forms.ModelForm):
    class Meta:
        model = TechType
        fields = ['name', 'descr']


class EngineTypeForm(forms.ModelForm):
    class Meta:
        model = EngineType
        fields = ['name', 'descr']


class GearTypeForm(forms.ModelForm):
    class Meta:
        model = GearType
        fields = ['name', 'descr']


class DriveAxelTypeForm(forms.ModelForm):
    class Meta:
        model = DriveAxelType
        fields = ['name', 'descr']


class SteerAxelTypeForm(forms.ModelForm):
    class Meta:
        model = SteerAxelType
        fields = ['name', 'descr']


class ServiceFirmForm(forms.ModelForm):
    class Meta:
        model = ServiceFirm
        fields = ['name', 'descr']


class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = ['name', 'descr']


class RepairMethodForm(forms.ModelForm):
    class Meta:
        model = RepairMethod
        fields = ['name', 'descr']


class FailurePartForm(forms.ModelForm):
    class Meta:
        model = FailurePart
        fields = ['name', 'descr']


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = forms.ALL_FIELDS


class DatePickerInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, attrs=None):
        super().__init__(attrs=attrs, format="%Y-%m-%d")


class ServiceForm(forms.ModelForm):
    def __init__(self, user, **kwargs):
        role = get_role(user)
        permissions = user.silantpermissions

        super(ServiceForm, self).__init__(**kwargs)

        f_vehicle = self.fields['vehicle']
        f_service = self.fields['service_firm']
        vehicle = Vehicle.objects.all()
        service = ServiceFirm.objects.all()
        match role:
            case 'MANAGER':
                f_vehicle.queryset = vehicle
                f_service.queryset = service
            case 'CLIENT':
                f_vehicle.queryset = vehicle.filter(client=permissions.client)
                f_service.queryset = service.none()
                f_service.widget = forms.HiddenInput()
            case 'SERVICE':
                f_vehicle.queryset = vehicle.filter(service_firm=permissions.service_firm)
                f_service.queryset = service.filter(pk=permissions.service_firm.pk)
                f_service.initial = permissions.service_firm
                f_service.widget = forms.HiddenInput()

    class Meta:
        model = Service
        fields = [
            'vehicle',
            'service_type',
            'date',
            'hours',
            'order_number',
            'order_date',
            'service_firm',
        ]
        widgets = {
            'date': DatePickerInput,
            'order_date': DatePickerInput,
        }


class ClaimForm(forms.ModelForm):
    def __init__(self, user, **kwargs):
        role = get_role(user)
        permissions = user.silantpermissions

        super(ClaimForm, self).__init__(**kwargs)

        f_vehicle = self.fields['vehicle']
        f_service = self.fields['service_firm']
        vehicle = Vehicle.objects.all()
        service = ServiceFirm.objects.all()
        match role:
            case 'MANAGER':
                f_vehicle.queryset = vehicle
                f_service.queryset = service
            case 'CLIENT':
                raise Exception('У клиента нет прав на создание и редактирование рекламаций')
            case 'SERVICE':
                f_vehicle.queryset = vehicle.filter(service_firm=permissions.service_firm)
                f_service.queryset = service.filter(pk=permissions.service_firm.pk)
                f_service.initial = permissions.service_firm
                f_service.widget = forms.HiddenInput()

    class Meta:
        model = Claim
        fields = [
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
        widgets = {
            'failure_date': DatePickerInput,
            'repaired_date': DatePickerInput,
        }

