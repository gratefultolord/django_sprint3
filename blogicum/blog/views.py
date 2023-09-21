from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone
from django.db.models import Q


def query_set():
    """Базовая функция view-функций приложения blog"""
    return Post.objects.select_related(
        'author', 'category', 'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    template = 'blog/index.html'
    posts = query_set().order_by('-pub_date')[:5]
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    selected_post = get_object_or_404(
        query_set(),
        pk=pk)
    context = {'post': selected_post}
    return render(request, template, context)


def category_posts(request, category):
    template = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category,
                                 is_published=True)
    category_posts = query_set().filter(category=category)
    context = {
        'category': category,
        'post_list': category_posts
    }
    return render(request, template, context)