from blog.models import Post

from django.utils import timezone


def query_set():
    """Базовая функция view-функций приложения blog."""
    return Post.objects.select_related(
        'author', 'category', 'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
