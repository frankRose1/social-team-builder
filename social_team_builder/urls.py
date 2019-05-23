from django.urls import path
from . import views

app_name = 'social_team_builder'

url_patterns = [
  path('', views.index, name='home'),
  path('signup/', views.sign_up, name='sign_up'),
  path('signin/', views.sign_in, name='sign_in')
]