from django.http import Http404
from django.shortcuts import render
from .models import App


def view_post(request, post_id):
    try:
        post = App.objects.get(pk=post_id)
    except App.DoesNotExist:
        raise Http404("Poll does not exist")

    return render(request, 'post.html', context={'post': post})
