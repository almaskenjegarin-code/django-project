from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название пункта")
    address = models.CharField(max_length=300, blank=True, verbose_name="Адрес")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    working_hours = models.CharField(max_length=100, blank=True, verbose_name="Время работы (Пн-Вс)", help_text="Например: Пн-Пт: 09:00 - 18:00")
    
    accepts_plastic = models.BooleanField(default=False, verbose_name="Принимает пластик")
    accepts_glass = models.BooleanField(default=False, verbose_name="Принимает стекло")
    accepts_paper = models.BooleanField(default=False, verbose_name="Принимает макулатуру")
    accepts_batteries = models.BooleanField(default=False, verbose_name="Принимает батарейки/электронику")

    class Meta:
        verbose_name = "Пункт приёма"
        verbose_name_plural = "Пункты приёма"

    def __str__(self):
        return self.name
