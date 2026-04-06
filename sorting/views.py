from django.shortcuts import render
from .models import Category

def sorting_info(request):
    categories = Category.objects.prefetch_related('rules').all()
    return render(request, 'sorting_info.html', {'categories': categories})
