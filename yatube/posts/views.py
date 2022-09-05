from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from yatube.settings import POSTS_LIMIT
from .models import Post, Group, User


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, POSTS_LIMIT) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/index.html'
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    paginator = Paginator(post_list, POSTS_LIMIT) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=author)
    post_counter = Post.objects.filter(author=author).count()
    paginator = Paginator(post_list, POSTS_LIMIT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title = f'Личная страница пользователя {username}'
    template = 'posts/profile.html'
    context = {
        'title': title,
        'author': author,
        'page_obj': page_obj,
        'post_counter': post_counter,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    author_post = post.author
    post_counter = Post.objects.filter(author=author_post).count()
    title = f'Пост {post.text[0:30]}'
    template = 'posts/post_detail.html'
    context = {
        'title': title,
        'post': post,
        'author_post': author_post,
        'post_counter': post_counter,
        'post_id': post_id,
    }
    return render(request, template, context)
