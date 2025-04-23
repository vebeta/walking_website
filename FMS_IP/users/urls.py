from django.urls import path
from .views import *

urlpatterns = [
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('profile', profile, name='profile'),
    path('logout', logout_user, name='logout'),
    path('password_reset', password_reset, name='password_reset'),
]
