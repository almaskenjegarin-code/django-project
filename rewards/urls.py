from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='rewards_catalog'),
    path('<int:pk>/buy/', views.buy_reward, name='buy_reward'),
]
