from django.urls import path
from .views import *

urlpatterns = [
    path('v1/', AppAPIView.as_view()),
    path('v1/post/', AppAPIPost.as_view()),
    path('v1/<int:pk>/', AppAPIDetail.as_view()),
    path('v1/top10/', AppAPIViewTop10.as_view()),
    path('v1/search/', AppAPIViewSearch.as_view()),
]
