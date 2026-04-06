from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Reward, Purchase
from .serializers import RewardSerializer, PurchaseSerializer

class RewardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reward.objects.filter(is_active=True)
    serializer_class = RewardSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def purchase(self, request, pk=None):
        reward = self.get_object()
        user_profile = request.user.profile
        
        if user_profile.eco_coins >= reward.cost:
            # Deduct coins
            user_profile.eco_coins -= reward.cost
            user_profile.save()
            
            # Create purchase record
            purchase = Purchase.objects.create(user=request.user, reward=reward)
            return Response({'status': 'success', 'message': 'Reward purchased'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'message': 'Not enough EcoCoins'}, status=status.HTTP_400_BAD_REQUEST)

class MyPurchasesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user).order_by('-date_purchased')
