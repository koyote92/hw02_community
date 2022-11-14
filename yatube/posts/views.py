from django.shortcuts import render, get_object_or_404
from .models import Post, Group


ORDER_BY_CONST: int = 10


def index(request):
    template = 'posts/index.html'
    posts = (
        Post.objects.order_by('-pub_date')
        .select_related('author')[:ORDER_BY_CONST]
    )
    # Получается, мы делаем select_related() по FK, который указан в models.py?
    return render(request, template, {
        'title': 'Последние обновления на сайте',
        'posts': posts,
    }
                  )


def group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    group_posts = Post.objects.filter(group=group)
    posts_ordered = (
        group_posts.order_by('-pub_date')
        .select_related('group')[:ORDER_BY_CONST]
    )
    # Если я правильно понял, prefetch_related() целесообразно использовать
    # для полей ManyToMany.
    # Насчёт вынесения сортировки в метакласс сил нет читать, заболел кажись.
    # Исправил (вроде) всё, что смог.
    return render(request, 'posts/group_list.html', {
        'title': 'Все записи сообщества',
        'group': group,
        'group_posts': group_posts,
        'posts': posts_ordered,
    }
                  )
