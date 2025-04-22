from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('about', about, name='about'),

    path('user/register', RegisterUser.as_view(), name='register'),
    path('user/login', LoginUser.as_view(), name='login'),
    path('user/profile', profile, name='profile'),
    path('user/logout', logout_user, name='logout'),
]
