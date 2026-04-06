from django.contrib import admin
from .models import Category, SortingRule

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'icon_class')

@admin.register(SortingRule)
class SortingRuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_recyclable')
    list_filter = ('category', 'is_recyclable')
