from rest_framework import serializers
from .models import Reward, Purchase

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    reward = RewardSerializer(read_only=True)
    
    class Meta:
        model = Purchase
        fields = ['id', 'reward', 'date_purchased']
