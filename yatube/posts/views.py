from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post, Group

# Create your views here.


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': 'Последние обновления на сайте',
        'posts': posts,
    }
    return render(request, template, context)


def group(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': 'Все записи сообщества',
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
