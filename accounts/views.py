from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
from .models import UserProfile

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан! Теперь вы можете войти.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def leaderboard(request):
    top_users = UserProfile.objects.select_related('user').order_by('-eco_coins')[:50]
    return render(request, 'accounts/leaderboard.html', {'top_users': top_users})
