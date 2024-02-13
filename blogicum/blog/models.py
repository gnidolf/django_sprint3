from django.db import models
from django.contrib.auth import get_user_model

from core.models import PublishedModel, CreateAtModel
from .constants import MAX_LENGTH_NAME


User = get_user_model()


class Location(PublishedModel, CreateAtModel):
    name = models.CharField(verbose_name='Название места',
                            max_length=MAX_LENGTH_NAME)

    class Meta():
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Category(PublishedModel, CreateAtModel):
    title = models.CharField(max_length=MAX_LENGTH_NAME,
                             verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.' # noqa
    )

    class Meta():
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(PublishedModel, CreateAtModel):
    title = models.CharField(max_length=MAX_LENGTH_NAME,
                             verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата и время публикации',
        help_text=('Если установить дату и время в будущем'
                   ' — можно делать отложенные публикации.')
    )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=False,
                               verbose_name='Автор публикации'
                               )
    location = models.ForeignKey(Location,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 verbose_name='Местоположение',
                                 )
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=False,
                                 verbose_name='Категория',
                                 related_name='posts'
                                 )

    class Meta():
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title
