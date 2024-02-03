from django.shortcuts import render
from .models import Location, Category, Post
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
    if pk not in posts_dict:
        raise Http404('что-то пошло не так')
    context = {'post': posts_dict[pk]}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = Category.objects.filter()
    context = {'category': category}
    return render(request, template, context)
