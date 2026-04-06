from django.contrib import admin
from .models import Reward, Purchase

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'reward', 'date_purchased')
    list_filter = ('date_purchased',)
    search_fields = ('user__username', 'reward__title')
