from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    ordering = '-published_at'
    article_list = Article.objects.order_by(ordering)
    template = 'articles/news.html'
    context = {
        'object_list': article_list,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)
