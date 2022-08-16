from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    posts = Post.objects.select_related('group')[:settings.NUMBER_OBJECTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
  #  posts = Post.objects.all()[:settings.NUMBER_OBJECTS]
    posts = group.posts.all()[:settings.NUMBER_OBJECTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
