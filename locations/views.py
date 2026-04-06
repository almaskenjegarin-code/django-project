from django.shortcuts import render
from .models import Location

# Create your views here.

def home(request):
    # placeholder card view
    return render(request, 'locations/home.html')


def location_list(request):
    locations = Location.objects.all()
    return render(request, 'locations/list.html', {'locations': locations})
