from rest_framework import viewsets, permissions
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().prefetch_related('rules')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
