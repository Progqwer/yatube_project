from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главнвя страница')

def group_posts(requests, any_slug):
    return HttpResponse(f'Группа под названием {any_slug}')



