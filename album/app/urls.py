from django.urls import path
from .views import *

urlpatterns = [
    path('1',view_post, name='view_post'),
]