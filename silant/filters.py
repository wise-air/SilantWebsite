from django_filters import FilterSet, CharFilter, ModelChoiceFilter

from .models import *


class VehicleFilter(FilterSet):
    vehicle_number = CharFilter(lookup_expr='icontains', label='Зав. № машины')
    tech_type = ModelChoiceFilter(queryset=TechType.objects.all())
    engine_type = ModelChoiceFilter(queryset=EngineType.objects.all())
    gear_type = ModelChoiceFilter(queryset=GearType.objects.all())
    drive_axel_type = ModelChoiceFilter(queryset=DriveAxelType.objects.all())
    steer_axel_type = ModelChoiceFilter(queryset=SteerAxelType.objects.all())

    class Meta:
        model = Vehicle
        fields = [
            'vehicle_number',
            'tech_type',
            'engine_type',
            'gear_type',
            'drive_axel_type',
            'steer_axel_type',
        ]


class ServiceFilter(FilterSet):
    vehicle__vehicle_number = CharFilter(lookup_expr='icontains', label='Зав. № машины')
    service_type = ModelChoiceFilter(queryset=ServiceType.objects.all())
    service_firm = ModelChoiceFilter(queryset=ServiceFirm.objects.all())

    class Meta:
        model = Vehicle
        fields = [
            'vehicle__vehicle_number',
            'service_type',
            'service_firm',
        ]


class ClimeFilter(FilterSet):
    vehicle__vehicle_number = CharFilter(lookup_expr='icontains', label='Зав. № машины')
    failure_part = ModelChoiceFilter(queryset=FailurePart.objects.all())
    repair_method = ModelChoiceFilter(queryset=RepairMethod.objects.all())
    service_firm = ModelChoiceFilter(queryset=ServiceFirm.objects.all())

    class Meta:
        model = Vehicle
        fields = [
            'vehicle__vehicle_number',
            'failure_part',
            'repair_method',
            'service_firm',
         ]

