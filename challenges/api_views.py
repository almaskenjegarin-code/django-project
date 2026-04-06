from rest_framework import viewsets, permissions
from .models import Challenge, ChallengeParticipation
from .serializers import ChallengeSerializer, ChallengeParticipationSerializer

class ChallengeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.AllowAny]

class MyChallengesViewSet(viewsets.ModelViewSet):
    serializer_class = ChallengeParticipationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ChallengeParticipation.objects.filter(user=self.request.user)
