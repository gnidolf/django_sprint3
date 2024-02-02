from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    context = {'posts': posts}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    if pk not in posts_dict:
        raise Http404('что-то пошло не так')
    context = {'post': posts_dict[pk]}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category': category_slug}
    return render(request, template, context)
