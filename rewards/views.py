from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reward, Purchase

def catalog(request):
    rewards = Reward.objects.filter(is_active=True).order_by('cost')
    return render(request, 'rewards/catalog.html', {'rewards': rewards})

@login_required
def buy_reward(request, pk):
    reward = get_object_or_404(Reward, pk=pk, is_active=True)
    user_profile = request.user.profile
    
    if request.method == 'POST':
        if user_profile.eco_coins >= reward.cost:
            # Deduct coins and record purchase
            user_profile.eco_coins -= reward.cost
            user_profile.save()
            Purchase.objects.create(user=request.user, reward=reward)
            messages.success(request, f'Вы успешно приобрели: {reward.title}!')
        else:
            messages.error(request, 'Недостаточно EcoCoins для покупки этой награды.')
            
    return redirect('rewards_catalog')
