from django.template import Template, Context
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from album.celery import app
from .models import App

REPORT_TEMPLATE = """
Here's how you did till now:

{% for post in posts %}
        "{{ post.title }}": viewed {{ post.views }} times |

{% endfor %}
"""


@app.task
def send_view_count_report():
    for user in get_user_model().objects.all():
        posts = App.objects.order_by('-views')[:3]
        if not posts:
            continue

        template = Template(REPORT_TEMPLATE)

        send_mail(
            'You won blablabla',
            template.render(context=Context({'posts': posts})),
            'asessor1982@gmail.com',
            [user.email],
            fail_silently=False,
        )