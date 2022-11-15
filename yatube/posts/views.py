from django.shortcuts import render, get_object_or_404
from .models import Post, Group


NUMBER_OF_POSTS: int = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.select_related('author')[:NUMBER_OF_POSTS]
    return render(request, template, {
        'title': 'Последние обновления на сайте',
        'posts': posts,
    })


def group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts_ordered = group.posts.select_related('author')[:NUMBER_OF_POSTS]
    return render(request, 'posts/group_list.html', {
        'title': 'Все записи сообщества',
        'group': group,
        'posts': posts_ordered,
    })
