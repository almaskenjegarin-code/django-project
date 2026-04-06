from rest_framework import serializers
from .models import Category, SortingRule

class SortingRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortingRule
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    rules = SortingRuleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon_class', 'order', 'rules']
