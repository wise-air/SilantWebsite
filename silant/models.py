from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, verbose_name='Наименование')
    descr = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class TechType(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, verbose_name='Наименование')
    descr = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'


class EngineType(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, verbose_name='Наименование')
    descr = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателей'


class GearType(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, verbose_name='Наименование')
    descr = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трасмиссий'


class DriveAxelType(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, verbose_name='Наименование')
    descr = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущих мостов'


class SteerAxelType(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, verbose_name='Наименование')
    descr = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемых мостов'


class ServiceFirm(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, verbose_name='Наименование')
    descr = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'


class ServiceType(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, verbose_name='Наименование')
    descr = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Виды ТО'


class RepairMethod(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, verbose_name='Наименование')
    descr = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способы восстановления'


class FailurePart(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, verbose_name='Наименование')
    descr = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Узлы отказа'


class Vehicle(models.Model):
    tech_type = models.ForeignKey(to=TechType, null=False, on_delete=models.RESTRICT, verbose_name='Модель техники')
    vehicle_number = models.CharField(max_length=64, null=False, verbose_name='Зав. № машины')
    engine_type = models.ForeignKey(to=EngineType, null=False, on_delete=models.RESTRICT,
                                    verbose_name='Модель двигателя')
    engine_number = models.CharField(max_length=64, null=False, verbose_name='Зав. № двигателя')
    gear_type = models.ForeignKey(to=GearType, null=False, on_delete=models.RESTRICT, verbose_name='Модель трансмиссии')
    gear_number = models.CharField(max_length=64, null=False, verbose_name='Зав. № трансмиссии')
    drive_axel_type = models.ForeignKey(to=DriveAxelType, null=False, on_delete=models.RESTRICT,
                                        verbose_name='Модель ведущего моста')
    drive_axel_number = models.CharField(max_length=64, null=False, verbose_name='Зав. № ведущего моста')
    steer_axel_type = models.ForeignKey(to=SteerAxelType, null=False, on_delete=models.RESTRICT,
                                        verbose_name='Модель управляемого моста')
    steer_axel_number = models.CharField(max_length=64, null=False, verbose_name='Зав. № управляемого моста')
    contract = models.CharField(max_length=64, null=True, blank=True, verbose_name='Договор поставки, №, дата')
    shipping_date = models.DateField(null=False, verbose_name='Дата отгрузки с завода')
    consumer = models.CharField(max_length=64, null=False, verbose_name='Грузополучатель')
    address = models.CharField(max_length=128, null=False, verbose_name='Адрес поставки')
    equipment = models.TextField(null=True, blank=True, verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(to=Client, null=False, on_delete=models.RESTRICT, verbose_name='Клиент')
    service_firm = models.ForeignKey(to=ServiceFirm, null=False, on_delete=models.RESTRICT,
                                     verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.vehicle_number}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Service(models.Model):
    vehicle = models.ForeignKey(to=Vehicle, null=False, on_delete=models.RESTRICT, verbose_name='Машина')
    service_type = models.ForeignKey(to=ServiceType, null=False, on_delete=models.RESTRICT, verbose_name='Вид ТО')
    date = models.DateField(null=False, verbose_name='Дата проведения ТО')
    hours = models.PositiveIntegerField(null=False, verbose_name='Наработка, м/час')
    order_number = models.CharField(max_length=64, null=False, verbose_name='№ заказа-наряда')
    order_date = models.DateField(null=False, verbose_name='Дата заказа-наряда')
    service_firm = models.ForeignKey(to=ServiceFirm, null=True, blank=True, on_delete=models.RESTRICT,
                                     verbose_name='Сервисная компания', )

    def __str__(self):
        return f'{self.vehicle} {self.service_type} {self.date}'

    class Meta:
        verbose_name = 'ТО'
        verbose_name_plural = 'ТО'


class Claim(models.Model):
    vehicle = models.ForeignKey(to=Vehicle, null=False, on_delete=models.RESTRICT, verbose_name='Машина')
    failure_date = models.DateField(null=False, verbose_name='Дата отказа')
    hours = models.PositiveIntegerField(null=False, verbose_name='Наработка, м/час')
    failure_part = models.ForeignKey(to=FailurePart, null=False, on_delete=models.RESTRICT, verbose_name='Узел отказа')
    failure_type = models.TextField(null=False, verbose_name='Описание отказа')
    repair_method = models.ForeignKey(to=RepairMethod, null=False, on_delete=models.RESTRICT,
                                      verbose_name='Способ восстановления')
    spare = models.TextField(null=True, blank=True, verbose_name='Использованные запчасти')
    repaired_date = models.DateField(null=False, verbose_name='Дата восстановления')
    service_firm = models.ForeignKey(to=ServiceFirm, null=False, on_delete=models.RESTRICT,
                                     verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.vehicle} {self.failure_date}'

    @property
    def downtime(self):
        result = self.repaired_date - self.failure_date
        return self.repaired_date - self.failure_date

    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'


class SilantPermissions(models.Model):
    PERMISSION_CHOICE = (
        ('CLIENT', 'Клиент'),
        ('SERVICE', 'Сервисная организация'),
        ('MANAGER', 'Менеджер'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=16, null=False, choices=PERMISSION_CHOICE, verbose_name="Роль")
    client = models.ForeignKey(to=Client, null=True, blank=True, on_delete=models.RESTRICT, verbose_name="Клиент")
    service_firm = models.ForeignKey(to=ServiceFirm, null=True, blank=True, on_delete=models.RESTRICT, verbose_name="Сервисная организация")

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Право доступа'
        verbose_name_plural = 'Права доступа'

