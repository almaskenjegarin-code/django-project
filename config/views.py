from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def sorting_info(request):
    # static educational content
    return render(request, 'sorting_info.html')
