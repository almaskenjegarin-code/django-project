"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from sorting.views import sorting_info

urlpatterns = [
    path('', home, name='home'),
    path('sorting/', sorting_info, name='sorting_info'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('challenges/', include('challenges.urls')),
    path('locations/', include('locations.urls')),
    path('rewards/', include('rewards.urls')),
    
    # API Routes
    path('api/accounts/', include('accounts.api_urls')),
    path('api/challenges/', include('challenges.api_urls')),
    path('api/locations/', include('locations.api_urls')),
    path('api/rewards/', include('rewards.api_urls')),
    path('api/sorting/', include('sorting.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
