from turtle import title
from django.shortcuts import render
from .models import Post, Group
from django.shortcuts import render, get_object_or_404


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    title = 'YaTube'
    context = {
        'title': title,
        'text': 'Это главная страница YaTube',
        'posts': posts,
    }
    return render(request, template, context) 


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    title = 'Group'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта YaTube',
        'group': group,
        'posts': posts,
    }
    return render(request, template, context) 


