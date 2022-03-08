from PIL import Image

from rest_framework import generics
from app.permissions import IsAuthorOrReadOnly
from app.models import App
from .serializers import *


class AppAPIView(generics.ListAPIView):

    queryset = App.objects.all()
    serializer_class = AppGetSerializer


class AppAPIPost(generics.ListCreateAPIView):

    queryset = App.objects.all()
    serializer_class = AppPostDetailSerializer


class AppAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = App.objects.all()
    serializer_class = AppPostDetailSerializer


class AppAPIViewTop10(generics.ListAPIView):

    queryset = App.objects.order_by('-views')[:10]
    serializer_class = AppGetSerializer









