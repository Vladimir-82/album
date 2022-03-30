from django.urls import path
from .views import *

urlpatterns = [
    path('<int:post_id>/', view_post, name='view_post'),
]