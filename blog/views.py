# -*- coding:utf-8 -*-

import os

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.conf import settings
from django.core.cache import cache
from django.db.models.aggregates import Count
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from iseek_backend.settings import BASE_DIR
from .serializers import (TopicSerializer, TagSerializer, ArticleSerializer, SimpleArticleSerializer, )

import markdown

from .models import (Tag, Topic, Article)


class IndexView(generic.ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = 5
    # paginate_orphans = 3

    def get_ordering(self):
        ordering = super(self.__class__, self).get_ordering()
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return ('-views', '-update_date', '-id')
        return ordering


def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)

    update_time = article.update_time.strftime("%Y%m%d%H%M%S")
    md_key = '{}_md_{}'.format(article.id, update_time)
    cache_md = cache.get(md_key)
    if cache_md:
        md = cache_md
    else:
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            # TocExtension(slugify=slugify),
        ])
        cache.set(md_key, md, 60 * 60 * 12)
    article.text = md.convert(article.text)
    article.toc = md.toc    # 目录

    context = {
        'article': article
    }
    return render(request, 'detail.html', context=context)


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
    about_file = os.path.join(BASE_DIR, 'doc', 'about.md')
    file = open(about_file, 'r')

    md_key = '{}_md'.format('about')
    cache_md = cache.get(md_key)
    if cache_md:
        md = cache_md
    else:
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            # TocExtension(slugify=slugify),
        ])
        cache.set(md_key, md, 60 * 60 * 12)
    about_text = md.convert(file.read())
    return render(request, 'about.html', context={'about_text': about_text})


def topic(request, id):
    topic = get_object_or_404(Topic, pk=id)
    articles = Article.objects.filter(topic=topic)
    context = {
        'topic': topic,
        'articles': articles,
    }
    return render(request, 'topic.html', context=context)


def tag(request, id):
    tag = get_object_or_404(Tag, pk=id)
    articles = Article.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'articles': articles,
    }
    return render(request, 'tag.html', context=context)


class CustomPagination(PageNumberPagination):
    page_size = 10
    # page_size_query_param = 'page_size'


class TopicAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get_queryset(self):
        return Topic.objects.annotate(total=Count('article')).filter(total__gt=0)


class TagAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all().order_by('update_time')
    serializer_class = ArticleSerializer
    pagination_class = CustomPagination
    # paginate_by = getattr(settings, 'PAGE_LIMIT', 10)

    def get_queryset(self):
        topic_id = self.request.query_params.get('topic', None)
        tag_id = self.request.query_params.get('tag', None)

        qs = self.queryset
        if topic_id:
            topic_id = int(topic_id)
            qs = self.queryset.filter(topic__id=topic_id)

        if tag_id:
            tag_id = int(tag_id)
            qs = self.queryset.filter(tags__id=tag_id)

        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = SimpleArticleSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SimpleArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        article = serializer.data
        if not article:
            return Response({})

        utime = article['utime']
        md_key = '{}_md_{}'.format(article['id'], utime)
        cache_md = cache.get(md_key)
        if cache_md:
            md = cache_md
        else:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                # TocExtension(slugify=slugify),
            ])
            cache.set(md_key, md, 60 * 60 * 12)
        article['text'] = md.convert(article['text'])
        article['toc'] = md.toc  # 目录

        return Response(article)

