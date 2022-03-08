from django.http import HttpResponse
from rest_framework import generics, filters
from app.permissions import IsAuthorOrReadOnly
from .serializers import *


class AppAPIView(generics.ListAPIView):
    queryset = App.objects.all()
    serializer_class = AppGetSerializer


class AppAPIPost(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppPostDetailSerializer

    def post(self, request, *args, **kwargs):
        photo = request.data['photo']
        if photo.size > 5242880:
            return HttpResponse('File must be less then 5 MiB!!!')
        photo = str(photo)
        if not photo.lower().endswith(('png', 'jpg', 'jpeg')):
            return HttpResponse('File not supported!!!')
        return super().post(request, *args, **kwargs)


class AppAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthorOrReadOnly]
    queryset = App.objects.all()
    serializer_class = AppPostDetailSerializer

    def get_object(self):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj


class AppAPIViewTop10(generics.ListAPIView):
    queryset = App.objects.order_by('-views')[:10]
    serializer_class = AppGetSerializer


class AppAPIViewSearch(generics.ListAPIView):
    queryset = App.objects.all()
    serializer_class = AppGetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author',]
