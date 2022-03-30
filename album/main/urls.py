from django.urls import path
from .views import home, verify


urlpatterns = [
    path('', home, name='home'),
    path('verify/(?P<uuid>[a-z0-9\-]+)/', verify, name='verify'),
]