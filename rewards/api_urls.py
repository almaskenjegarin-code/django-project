from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import RewardViewSet, MyPurchasesViewSet

router = DefaultRouter()
router.register(r'shop', RewardViewSet, basename='reward')
router.register(r'my-purchases', MyPurchasesViewSet, basename='my-purchases')

urlpatterns = [
    path('', include(router.urls)),
]
