from django.urls import path, re_path
from .views import home, verify


urlpatterns = [
    path('', home, name='home'),
    path('verify/(?P<uuid>[0-9]+)/\\Z', verify, name='verify'),
]