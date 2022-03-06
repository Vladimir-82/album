from rest_framework import generics
from app.models import App
from .serializers import AppSerializer
from PIL import Image




class AppAPIView(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    # for ph in App.objects.all():
    #     if not ph.photo_webp:
    #         im = Image.open(ph.photo)
    #         width, height = im.size
    #         if width > height:
    #             new_width = 150
    #             new_height = int(new_width * height / width)
    #         else:
    #             new_height = 150
    #             new_width = int(new_height * width / height)
    #         res = im.resize((new_width, new_height), Image.ANTIALIAS)
    #         ph.photo_webp = res
    #         ph.save()
    # for i in App.objects.all():
    #     print(i.photo_webp)
    # queryset = App.objects.all()



class AppAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer



