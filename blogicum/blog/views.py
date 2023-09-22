from django.shortcuts import render, get_object_or_404

from blog.models import Category

from blog.querysets import query_set


def index(request):
    POSTS_PER_PAGE = 5
    posts = query_set().order_by('-pub_date')[:POSTS_PER_PAGE]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, pk):
    selected_post = get_object_or_404(
        query_set(),
        pk=pk)
    context = {'post': selected_post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category):
    category = get_object_or_404(Category,
                                 slug=category,
                                 is_published=True)
    category_posts = query_set().filter(category=category)
    context = {
        'category': category,
        'post_list': category_posts
    }
    return render(request, 'blog/category.html', context)
