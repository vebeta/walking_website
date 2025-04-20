from django.urls import path
from .views import *

urlpatterns = [
    path('', TrailsHome.as_view(), name='trails'),
    path('trail/<slug:trl_slug>', TrailPage.as_view(), name='trail'),
    path('addtrail', AddTrail.as_view(), name='addtrail')
]
