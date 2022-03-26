from __future__ import absolute_import
import os
import celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'album.settings')

app = celery.Celery("album")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def add(x, y):
    return x / y