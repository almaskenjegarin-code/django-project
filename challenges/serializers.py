from rest_framework import serializers
from .models import Challenge, ChallengeParticipation

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'

class ChallengeParticipationSerializer(serializers.ModelSerializer):
    challenge = ChallengeSerializer(read_only=True)
    
    class Meta:
        model = ChallengeParticipation
        fields = ['id', 'challenge', 'joined_at', 'is_completed', 'proof_image']
