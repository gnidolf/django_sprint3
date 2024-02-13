from datetime import datetime

from django.shortcuts import render, get_object_or_404

from .models import Category, Post


def base_filter(queryset):
    result = queryset.select_related('location', 'category').filter(
        is_published=True,
        pub_date__lt=datetime.now(),
        category__is_published=True,
    )
    return result


def index(request):
    template = 'blog/index.html'
    queryset = base_filter(Post.objects)[:5]
    context = {'post_list': queryset}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    queryset = base_filter(Post.objects)
    post = get_object_or_404(queryset, pk=pk)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True,
                                 created_at__lt=datetime.now()
                                 )

    queryset = base_filter(category.posts)

    context = {'category': category, 'post_list': queryset}
    return render(request, template, context)
