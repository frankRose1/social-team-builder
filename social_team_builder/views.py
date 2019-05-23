from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'social_team_builder/index.html')


def sign_up(request):
    return render(request, 'social_team_builder/signup.html')


def sign_in(request):
    return render(request, 'social_team_builder/signin.html')