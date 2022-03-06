from rest_framework import generics
from app.models import App
from .serializers import AppSerializer
from PIL import Image




class AppAPIView(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class AppAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer



