from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ChallengeViewSet, MyChallengesViewSet

router = DefaultRouter()
router.register(r'all', ChallengeViewSet, basename='challenge')
router.register(r'my', MyChallengesViewSet, basename='my-challenges')

urlpatterns = [
    path('', include(router.urls)),
]
