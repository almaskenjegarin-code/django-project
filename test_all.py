import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.conf import settings
settings.ALLOWED_HOSTS = ['*']

from django.test import Client
from django.urls import reverse

client = Client()

urls = [
    '/',
    '/sorting/',
    '/accounts/',
    '/accounts/login/',
    '/accounts/register/',
    '/challenges/',
    '/challenges/1/',
    '/locations/',
]

for url in urls:
    try:
        response = client.get(url)
        print(f"GET {url} - {response.status_code}")
    except Exception as e:
        print(f"GET {url} - ERROR: {e}")

try:
    response = client.post('/accounts/register/', {
        'username': 'testuser',
        'email': 'test@test.com',
        'password1': 'StrongPass123!',
        'password2': 'StrongPass123!'
    })
    print(f"POST /accounts/register/ - {response.status_code}")
except Exception as e:
    print(f"POST /accounts/register/ - ERROR: {e}")
