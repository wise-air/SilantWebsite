from django.urls import path, re_path, include
from django.views.generic import RedirectView
from rest_framework.schemas import get_schema_view

from .views import *

silant_urls = [
    path('', RedirectView.as_view(url='/vehicle'), name="silant.main"),

    path('openapi', get_schema_view(
        title="Silant",
        version="1.0.0"
    ), name='silant.openapi'),
    path('openapi/vehicle', VehicleListAPIView.as_view(), name='silant.vehicle.api'),
    path('openapi/service', ServiceListAPIView.as_view(), name='silant.service.api'),
    path('openapi/claim', ClaimListAPIView.as_view(), name='silant.claim.api'),

    path('vehicle/', VehicleListView.as_view(), name="silant.vehicle.list"),
    path('vehicle/add', VehicleAddView.as_view(), name="silant.vehicle.add"),
    path('vehicle/<int:pk>', VehicleDetailView.as_view(), name="silant.vehicle.detail"),
    path('vehicle/<int:pk>/edit', VehicleUpdateView.as_view(), name="silant.vehicle.update"),
    path('vehicle/<int:pk>/delete', VehicleDeleteView.as_view(), name="silant.vehicle.delete"),

    path('service/', ServiceListView.as_view(), name="silant.service.list"),
    path('service/add', ServiceAddView.as_view(), name="silant.service.add"),
    path('service/<int:pk>', ServiceDetailView.as_view(), name="silant.service.detail"),
    path('service/<int:pk>/edit', ServiceUpdateView.as_view(), name="silant.service.update"),
    path('service/<int:pk>/delete', ServiceDeleteView.as_view(), name="silant.service.delete"),

    path('claim/', ClaimListView.as_view(), name="silant.claim.list"),
    path('claim/add', ClaimAddView.as_view(), name="silant.claim.add"),
    path('claim/<int:pk>', ClaimDetailView.as_view(), name="silant.claim.detail"),
    path('claim/<int:pk>/edit', ClaimUpdateView.as_view(), name="silant.claim.update"),
    path('claim/<int:pk>/delete', ClaimDeleteView.as_view(), name="silant.claim.delete"),

    path('client/', ClientListView.as_view(), name="silant.client.list"),
    path('client/add', ClientAddView.as_view(), name="silant.client.add"),
    path('client/<int:pk>', ClientDetailView.as_view(), name="silant.client.detail"),
    path('client/<int:pk>/edit', ClientUpdateView.as_view(), name="silant.client.update"),
    path('client/<int:pk>/delete', ClientDeleteView.as_view(), name="silant.client.delete"),

    path('tech_type/', TechTypeListView.as_view(), name="silant.tech_type.list"),
    path('tech_type/add', TechTypeAddView.as_view(), name="silant.tech_type.add"),
    path('tech_type/<int:pk>', TechTypeDetailView.as_view(), name="silant.tech_type.detail"),
    path('tech_type/<int:pk>/edit', TechTypeUpdateView.as_view(), name="silant.tech_type.update"),
    path('tech_type/<int:pk>/delete', TechTypeDeleteView.as_view(), name="silant.tech_type.delete"),

    path('engine_type/', EngineTypeListView.as_view(), name="silant.engine_type.list"),
    path('engine_type/add', EngineTypeAddView.as_view(), name="silant.engine_type.add"),
    path('engine_type/<int:pk>', EngineTypeDetailView.as_view(), name="silant.engine_type.detail"),
    path('engine_type/<int:pk>/edit', EngineTypeUpdateView.as_view(), name="silant.engine_type.update"),
    path('engine_type/<int:pk>/delete', EngineTypeDeleteView.as_view(), name="silant.engine_type.delete"),

    path('gear_type/', GearTypeListView.as_view(), name="silant.gear_type.list"),
    path('gear_type/add', GearTypeAddView.as_view(), name="silant.gear_type.add"),
    path('gear_type/<int:pk>', GearTypeDetailView.as_view(), name="silant.gear_type.detail"),
    path('gear_type/<int:pk>/edit', GearTypeUpdateView.as_view(), name="silant.gear_type.update"),
    path('gear_type/<int:pk>/delete', GearTypeDeleteView.as_view(), name="silant.gear_type.delete"),

    path('drive_axel_type/', DriveAxelTypeListView.as_view(), name="silant.drive_axel_type.list"),
    path('drive_axel_type/add', DriveAxelTypeAddView.as_view(), name="silant.drive_axel_type.add"),
    path('drive_axel_type/<int:pk>', DriveAxelTypeDetailView.as_view(), name="silant.drive_axel_type.detail"),
    path('drive_axel_type/<int:pk>/edit', DriveAxelTypeUpdateView.as_view(), name="silant.drive_axel_type.update"),
    path('drive_axel_type/<int:pk>/delete', DriveAxelTypeDeleteView.as_view(), name="silant.drive_axel_type.delete"),

    path('steer_axel_type/', SteerAxelTypeListView.as_view(), name="silant.steer_axel_type.list"),
    path('steer_axel_type/add', SteerAxelTypeAddView.as_view(), name="silant.steer_axel_type.add"),
    path('steer_axel_type/<int:pk>', SteerAxelTypeDetailView.as_view(), name="silant.steer_axel_type.detail"),
    path('steer_axel_type/<int:pk>/edit', SteerAxelTypeUpdateView.as_view(), name="silant.steer_axel_type.update"),
    path('steer_axel_type/<int:pk>/delete', SteerAxelTypeDeleteView.as_view(), name="silant.steer_axel_type.delete"),

    path('service_firm/', ServiceFirmListView.as_view(), name="silant.service_firm.list"),
    path('service_firm/add', ServiceFirmAddView.as_view(), name="silant.service_firm.add"),
    path('service_firm/<int:pk>', ServiceFirmDetailView.as_view(), name="silant.service_firm.detail"),
    path('service_firm/<int:pk>/edit', ServiceFirmUpdateView.as_view(), name="silant.service_firm.update"),
    path('service_firm/<int:pk>/delete', ServiceFirmDeleteView.as_view(), name="silant.service_firm.delete"),

    path('service_type/', ServiceTypeListView.as_view(), name="silant.service_type.list"),
    path('service_type/add', ServiceTypeAddView.as_view(), name="silant.service_type.add"),
    path('service_type/<int:pk>', ServiceTypeDetailView.as_view(), name="silant.service_type.detail"),
    path('service_type/<int:pk>/edit', ServiceTypeUpdateView.as_view(), name="silant.service_type.update"),
    path('service_type/<int:pk>/delete', ServiceTypeDeleteView.as_view(), name="silant.service_type.delete"),

    path('repair_method/', RepairMethodListView.as_view(), name="silant.repair_method.list"),
    path('repair_method/add', RepairMethodAddView.as_view(), name="silant.repair_method.add"),
    path('repair_method/<int:pk>', RepairMethodDetailView.as_view(), name="silant.repair_method.detail"),
    path('repair_method/<int:pk>/edit', RepairMethodUpdateView.as_view(), name="silant.repair_method.update"),
    path('repair_method/<int:pk>/delete', RepairMethodDeleteView.as_view(), name="silant.repair_method.delete"),

    path('failure_part/', FailurePartListView.as_view(), name="silant.failure_part.list"),
    path('failure_part/add', FailurePartAddView.as_view(), name="silant.failure_part.add"),
    path('failure_part/<int:pk>', FailurePartDetailView.as_view(), name="silant.failure_part.detail"),
    path('failure_part/<int:pk>/edit', FailurePartUpdateView.as_view(), name="silant.failure_part.update"),
    path('failure_part/<int:pk>/delete', FailurePartDeleteView.as_view(), name="silant.failure_part.delete"),

    path('hand_book_vehicle/', HandBkListVehicleView.as_view(), name="silant.handbk_vehicle.list"),
    path('hand_book_service/', HandBkListServiceView.as_view(), name="silant.handbk_service.list"),
    path('hand_book_claim/', HandBkListClaimView.as_view(), name="silant.handbk_claim.list"),
]
