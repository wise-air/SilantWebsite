from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(SilantPermissions)
class SilantPermissionsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'role',
        'client',
        'service_firm',
    )


class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('name', 'descr')


admin.site.register(Client, VocabularyAdmin)
admin.site.register(TechType, VocabularyAdmin)
admin.site.register(EngineType, VocabularyAdmin)
admin.site.register(GearType, VocabularyAdmin)
admin.site.register(RepairMethod, VocabularyAdmin)
admin.site.register(DriveAxelType, VocabularyAdmin)
admin.site.register(SteerAxelType, VocabularyAdmin)
admin.site.register(ServiceFirm, VocabularyAdmin)
admin.site.register(ServiceType, VocabularyAdmin)
admin.site.register(FailurePart, VocabularyAdmin)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
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
        # 'contract',
        'shipping_date__format',
        'client',
        'consumer',
        'address',
        'equipment',
        'service_firm',
    )

    def shipping_date__format(self, obj):
        return obj.shipping_date.strftime('%d.%m.%Y')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'vehicle',
        'service_type',
        'date__format',
        'hours',
        'order_number',
        'order_date__format',
        'service_firm__format',
    )

    def date__format(self, obj):
        return obj.date.strftime('%d.%m.%Y')

    def order_date__format(self, obj):
        return obj.order_date.strftime('%d.%m.%Y')

    def service_firm__format(self, obj):
        return obj.service_firm if obj.service_firm else 'самостоятельно'


@admin.register(Claim)
class ClimeAdmin(admin.ModelAdmin):
    list_display = (
        'vehicle',
        'failure_date__format',
        'hours',
        'failure_part',
        'failure_type',
        'repair_method',
        'spare',
        'repaired_date__format',
        'downtime_format',
        'service_firm',
    )

    def failure_date__format(self, obj):
        return obj.failure_date.strftime('%d.%m.%Y')

    def repaired_date__format(self, obj):
        return obj.repaired_date.strftime('%d.%m.%Y')

    def downtime_format(self, obj):
        downtime = obj.downtime
        return downtime.days
