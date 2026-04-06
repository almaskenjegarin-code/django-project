from django.contrib import admin
from .models import Location

# Register your models here.

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'working_hours', 'accepts_plastic', 'accepts_glass', 'accepts_paper', 'accepts_batteries')
    list_filter = ('accepts_plastic', 'accepts_glass', 'accepts_paper', 'accepts_batteries')
    search_fields = ('name', 'address')
