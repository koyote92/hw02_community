from django.urls import path

from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group, name='group'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_details'),
    # Код ниже в процессе разработки
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
]
