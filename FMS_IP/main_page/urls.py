from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),

    path('register', RegisterUser.as_view(), name='register'),
    path('login', login, name='login'),
    path('profile', profile, name='profile')
]
