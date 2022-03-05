from django.urls import path
from .views import AppAPIView, AppAPIDetail

urlpatterns = [
    path('v1', AppAPIView.as_view()),
    path('v1/<int:pk>', AppAPIDetail.as_view()),
]