from django.http import HttpResponse
from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework import permissions



class AppAPIView(generics.ListAPIView):
    queryset = App.objects.all()
    serializer_class = AppGetSerializer


class AppAPIPost(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
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
    permission_classes = (permissions.IsAuthenticated,)
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


class AppAPIViewTop3(generics.ListAPIView):
    queryset = App.objects.order_by('-views')[:3]
    serializer_class = AppGetSerializer




class AppAPIViewSearch(generics.ListAPIView):
    queryset = App.objects.all()
    serializer_class = AppGetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author',]



# jwt
class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Паттерн создания сериализатора, валидации и сохранения - довольно
        # стандартный, и его можно часто увидеть в реальных проектах.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
