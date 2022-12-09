from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .forms import PostEditionForm, PostCreationForm
from .models import Post, Group, User


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
    paginator = Paginator(group_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/group_post.html', {
        'title': 'Все записи сообщества',
        'group': group,
        'posts': group_posts,
        'page_obj': page_obj,
    })


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = author.posts.select_related('author')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


"""Код ниже в процессе разработки."""


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'posts/post_details.html', context)


def post_edit(request, post_id):
    if request.method == 'POST':
        form = PostEditionForm(request.POST)
        if not form.is_valid():
            form = PostEditionForm()
            return render(request, 'posts/index.html', {'form': form})
        form = PostEditionForm()
        text = form.cleaned_data['text']
        group = form.cleaned_data['group']
        return redirect('posts/post_details.html', id=post_id)

    form = PostEditionForm()
    return render(request, 'posts/index.html', {'form': form})
