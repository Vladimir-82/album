from PIL import Image
from io import BytesIO

from django.db import models
from django.core.files.base import ContentFile


class App(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_webp = models.ImageField(upload_to='photos_webp/%Y/%m/%d/', blank=True, null=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        im = Image.open(self.photo)
        width, height = im.size
        if width > height:
            new_width = 150
            new_height = new_width * height // width
        else:
            new_height = 150
            new_width = new_height * width // height
        image = im.resize((new_width, new_height), Image.ANTIALIAS)
        buffer = BytesIO()
        image.save(fp=buffer, format='webp')
        self.photo_webp.save(name='img.webp', content=ContentFile(buffer.getvalue()), save=False)
        super().save(*args, **kwargs)



    def __str__(self):
        return self.title