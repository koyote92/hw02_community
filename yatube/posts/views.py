from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group


def index(request):
    posts = Post.objects.select_related('author')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/index.html', {
        'title': 'Последние обновления на сайте',
        'posts': posts,
        'page_obj': page_obj,
    })


def group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    group_posts = group.posts.select_related('author')
    return render(request, 'posts/group_list.html', {
        'title': 'Все записи сообщества',
        'group': group,
        'posts': group_posts,
    })
