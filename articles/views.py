from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


def search(request):
    queryset_list = Article.objects.order_by('-date')

    if 'tags' in request.GET:
        tags = request.GET['tags']
        if tags:
            queryset_list = queryset_list.filter(tags__icontains='hiking')
    context = {
        'tags': 'tags',
    }

    return render(request, 'articles/search.html', context)
