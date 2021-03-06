from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    # path('v1/', cache_page(2*60)(AppAPIView.as_view())),
    path('v1/', AppAPIView.as_view()),
    path('v1/post/', AppAPIPost.as_view()),
    path('v1/<int:pk>/', AppAPIDetail.as_view()),
    path('v1/top10/', AppAPIViewTop10.as_view()),
    path('v1/top3/', AppAPIViewTop3.as_view()),
    path('v1/search/', AppAPIViewSearch.as_view()),
    path('v1/users/', RegistrationAPIView.as_view()), # jwt
]
