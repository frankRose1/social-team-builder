from django.urls import path
from . import views

app_name = 'social_team_builder'

url_patterns = [
  path('', views.index, name='home')
]