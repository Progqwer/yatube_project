from django.contrib.auth import get_user_model
from django.db import models


class Group(models.Model):
    '''Модель таблицы группы'''
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Группы'

    def __str__(self):
        return self.title


User = get_user_model()


class Post(models.Model):
    '''Модель таблицы посты'''
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа',
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Посты'
        ordering = ['-pub_date']
