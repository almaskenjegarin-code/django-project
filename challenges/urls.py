from django.urls import path
from . import views

urlpatterns = [
    path('', views.challenge_list, name='challenges_home'),
    path('<int:pk>/', views.challenge_detail, name='challenge_detail'),
    path('<int:pk>/join/', views.join_challenge, name='join_challenge'),
    path('<int:pk>/complete/', views.complete_challenge, name='complete_challenge'),
]
