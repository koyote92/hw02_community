from django.shortcuts import render, get_object_or_404
from .models import Post, Group


NUMBER_OF_POSTS: int = 10


def index(request):
    posts = Post.objects.select_related('author')[:NUMBER_OF_POSTS]
    return render(request, 'posts/index.html', {
        'title': 'Последние обновления на сайте',
        'posts': posts,
    })


def group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    group_posts = group.posts.select_related('author')[:NUMBER_OF_POSTS]
    return render(request, 'posts/group_list.html', {
        'title': 'Все записи сообщества',
        'group': group,
        'posts': group_posts,
    })
