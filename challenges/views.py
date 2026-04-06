from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Challenge, ChallengeParticipation
from accounts.models import UserProfile

# Create your views here.

def home(request):
    # placeholder for home card
    return render(request, 'challenges/home.html')


def challenge_list(request):
    challenges = Challenge.objects.all().order_by('-start_date')
    return render(request, 'challenges/list.html', {'challenges': challenges})



def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    participation = None
    if request.user.is_authenticated:
        participation = ChallengeParticipation.objects.filter(challenge=challenge, user=request.user).first()
    return render(request, 'challenges/detail.html', {'challenge': challenge, 'participation': participation})

@login_required
def join_challenge(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    ChallengeParticipation.objects.get_or_create(user=request.user, challenge=challenge)
    return redirect('challenge_detail', pk=pk)

@login_required
def complete_challenge(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    participation = get_object_or_404(ChallengeParticipation, user=request.user, challenge=challenge)
    
    if request.method == 'POST':
        if not participation.is_completed:
            # Check if user uploaded a file
            if 'proof_image' in request.FILES:
                participation.proof_image = request.FILES['proof_image']
                participation.is_completed = True
                profile, _ = UserProfile.objects.get_or_create(user=request.user)
                profile.eco_coins += 50
                profile.save()
                participation.save()
            else:
                # Optionally add a message here, but basic flow requires image
                messages.error(request, 'Пожалуйста, загрузите фото-подтверждение.')
        else:
            # User is un-completing the challenge (optional feature, maybe we disable this for photos)
            # For now, let's keep it but remove the points and image
            participation.is_completed = False
            participation.proof_image = None
            profile, _ = UserProfile.objects.get_or_create(user=request.user)
            profile.eco_coins = max(0, profile.eco_coins - 50)
            profile.save()
            participation.save()
            
    return redirect('challenge_detail', pk=pk)
