from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from datetime import datetime


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.select_related('location', 'category').filter(
        is_published=True,
        pub_date__lt=datetime.now(),
        category__is_published=True,
    )[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post_list = Post.objects.select_related('location', 'category').filter(
        is_published=True,
        pub_date__lt=datetime.now(),
        category__is_published=True
    )
    post = get_object_or_404(post_list, pk=pk)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    post_list = Post.objects.select_related('location', 'category').filter(
        is_published=True,
        pub_date__lt=datetime.now(),
        category__is_published=True,
        category__slug=category_slug
    )
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True,
                                 created_at__lt=datetime.now()
                                 )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
