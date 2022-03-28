import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'album.settings')

app = Celery('album')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()