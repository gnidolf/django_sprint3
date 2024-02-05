from django.db import models
from core.models import PublishedModel
from django.contrib.auth import get_user_model


User = get_user_model()

class Location(PublishedModel):
    name = models.CharField(verbose_name='Название места', max_length=256)

    class Meta():
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание') 
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор', 
        help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta():
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
    
class Post(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        auto_now=False, 
        auto_now_add=False, 
        verbose_name='Дата и время публикации', 
        help_text='Если установить дату и время в будущем — можно делать отложенные публикации.'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='Автор публикации')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, verbose_name='Местоположение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Категория')

    class Meta():
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)




