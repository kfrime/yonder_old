# -*- coding:utf-8 -*-

import os
from collections import OrderedDict

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.conf import settings
from django.core.cache import cache
from django.db.models.aggregates import (Count, Q)
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action

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
    page_size = 8

    def get_paginated_response(self, data):
        _next = self.page.next_page_number() if self.page.has_next() else None
        _pre = self.page.previous_page_number() if self.page.has_previous() else None
        _count = self.page.paginator.count
        _size = self.page_size

        _pages = _count // _size if _count % _size == 0 else _count // _size + 1

        page = OrderedDict([
            ('count', _count),
            # ('last', self.page.paginator.count),
            # ('offset', _size),
            ('pages', _pages),
            ('pre', _pre),
            ('current', self.page.number),
            ('next', _next),
            # ('nextLink', self.get_next_link()),
            # ('preLink', self.get_previous_link())
        ])

        return Response(OrderedDict([
            ('page', page),
            ('results', data)
        ]))


class TopicAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.all().order_by('id')
    serializer_class = TopicSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Topic.objects.annotate(total=Count('article')).filter(total__gt=0)


class TagAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.exclude(article__isnull=True).annotate(total=Count('article')).order_by('id')
    serializer_class = TagSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        article_id = self.request.query_params.get('article', None)

        qs = self.queryset
        if article_id:
            article_id = int(article_id)
            qs = self.queryset.filter(article=article_id)

        return qs


class ArticleAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all().order_by('create_time')
    serializer_class = ArticleSerializer
    pagination_class = CustomPagination
    # paginate_by = getattr(settings, 'PAGE_LIMIT', 10)

    def get_queryset(self):
        topic_id = self.request.query_params.get('topic', None)
        tag_id = self.request.query_params.get('tag', None)
        search = self.request.query_params.get('search', None)

        qs = self.queryset
        if topic_id:
            topic_id = int(topic_id)
            qs = self.queryset.filter(topic=topic_id)

        if tag_id:
            tag_id = int(tag_id)
            qs = self.queryset.filter(tags=tag_id)

        if search:
            qs = Article.objects.filter(title__icontains=search)

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

        utime = article['utime'].split(' ')[0]      # date str
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

        _next = instance.get_next()
        _pre = instance.get_pre()
        article['next'] = {
            'id': _next.id,
            'title': _next.title
        } if _next else None
        article['pre'] = {
            'id': _pre.id,
            'title': _pre.title
        } if _pre else None
        return Response(article)

    @action(detail=False, methods=['get'], url_path='search')
    def search(self, request, *args, **kwargs):
        q = self.request.query_params.get('q', None)
        if not q:
            return Response({})

        qs = Article.objects.filter(Q(title__icontains=q) | Q(slug__icontains=q))
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = SimpleArticleSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SimpleArticleSerializer(qs, many=True)
        return Response(serializer.data)

