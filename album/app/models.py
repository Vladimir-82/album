from django.db import models



class App(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    photo_webp = models.ImageField(verbose_name='Фото', blank=True, null=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title