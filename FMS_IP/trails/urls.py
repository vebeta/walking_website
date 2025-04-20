from django.urls import path
from .views import *

urlpatterns = [
    path('', TrailsHome.as_view(), name='trails'),
    path('trail/<int:trl_id>', trail_page, name='trail'),
    path('addtrail', add_trail, name='addtrail')
]
