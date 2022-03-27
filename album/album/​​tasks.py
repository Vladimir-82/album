from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .celery import app
from app.models import App


@app.task
def send_view_count_report():
    for user in get_user_model().objects.all():
        post = App.objects.order_by('-views')[:3].filter(author=user)
        send_mail(
            'You take an abrakadabra',
            'from@top3.dev',
            [post.photo],
            [user.email],
            fail_silently=False,
        )