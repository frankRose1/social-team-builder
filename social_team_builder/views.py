from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q

from .models import UserProfile
from .forms import ProfileForm

# Create your views here.
def index(request):
    return render(request, 'social_team_builder/index.html')


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # create the user and log them in
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                'Your registration was a success! We signed you in too.'
            )
            return HttpResponseRedirect(reverse('team_builder:home'))
    return render(request, 'social_team_builder/signup.html', {'form': form})


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    messages.success(
                        request,
                        'You were successfully signed in.'
                    )
                    return HttpResponseRedirect(reverse('team_builder:home'))
                else:
                    messages.error(
                        request,
                        'This user account has been disabled.'
                    )
        else:
            messages.error(
                request,
                'Invalid email or password.'
            )
    return render(request, 'social_team_builder/signin.html', {'form': form})


@login_required
def sign_out(request):
    logout(request)
    messages.success(
        request,
        'You were successfully signed out. Come back soon!'
    )
    return HttpResponseRedirect(reverse('team_builder:home'))


# the user should be able to create a profile and upload an image
@login_required
def edit_user_profile(request):
    try:
        profile = UserProfile.objects.get(user_id=request.user.id)
        form = ProfileForm(instance=profile)
    except UserProfile.DoesNotExist:
        form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(
            instance=profile,
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your profile has been updated!'
            )
            return HttpResponseRedirect(reverse('team_builder:user_profile', kwargs={'user_id': request.user.id }))
    return render(request, 'social_team_builder/edit_profile.html' ,{'form': form})


def user_profile(request, user_id):
    """Gets a user's profile"""
    pass