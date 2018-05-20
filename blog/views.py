# -*- coding:utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import (Tag, Topic, Article)

# Create your views here.


def index(request):
    # return HttpResponse("Hello, world.")
    context = {
        'tags': Tag.objects.all(),
        'topics': Topic.objects.all().exclude(parent=None),
        'articles': Article.objects.all(),
    }
    return render(request, 'index.html', context=context)


def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        'article': article
    }
    return render(request, 'article_detail.html', context=context)


def article_list(request):
    tag_id = request.GET.get('tag_id', None)
    topic_id = request.GET.get('topic_id', None)
    articles = None
    if tag_id:
        articles = Article.objects.filter(tags=int(tag_id))
    if topic_id:
        articles = Article.objects.filter(topic_id=int(topic_id))

    context = {
        'articles': articles,
    }
    return render(request, 'article_list.html', context=context)


def about(request):
    return render(request, 'about.html')



