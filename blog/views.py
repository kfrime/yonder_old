# -*- coding: utf-8 -*-

import os
from collections import OrderedDict
import markdown
from django.db.models.aggregates import (Count, )
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action

from utils.const import c_visible as v
from .models import (Tag, Topic, Article)
from .serializers import (
    TopicSerializer, TagSerializer, ArticleSerializer, SimpleArticleSerializer,
    SmallArticleSerializer
)


class SmallPagination(PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):
        _next = self.page.next_page_number() if self.page.has_next() else None
        _pre = self.page.previous_page_number() if self.page.has_previous() else None
        _count = self.page.paginator.count
        _size = self.page_size

        _pages = _count // _size if _count % _size == 0 else _count // _size + 1

        page = OrderedDict([
            ('count', _count),
            ('pages', _pages),
            ('pre', _pre),
            ('current', self.page.number),
            ('next', _next),
            # ('last', self.page.paginator.count),
            # ('offset', _size),
            # ('nextLink', self.get_next_link()),
            # ('preLink', self.get_previous_link())
        ])

        return Response(OrderedDict([
            ('page', page),
            ('data', data)
        ]))


class BigPagination(SmallPagination):
    page_size = 200


# 如果某主题/标签不可见，则其下的文章也不可见
# 某主题/标签下的可见文章总数大于0，该主题才会被展示出来
# 要结合某篇文章的主题和标签是否可见来决定该文章是否可见
# 文章可显示：其本身，其主题，其关联的标签都要是可见的

class TopicAPIView(viewsets.ReadOnlyModelViewSet):
    # 只统计可显示的文章总数，某主题下有可显示的文章时，该主题才会展示出来
    queryset = Topic.objects.filter(
        visible=v.IS_VISIBLE,
        article__visible=v.IS_VISIBLE,
        # article__tags__visible=v.IS_VISIBLE      # 多对多关系的数据会有重复　
    ).exclude(
        article__tags__visible=v.NOT_VISIBLE
    ).annotate(
        total=Count('article')
    ).filter(total__gt=0).order_by('id')

    serializer_class = TopicSerializer
    pagination_class = BigPagination


class TagAPIView(viewsets.ReadOnlyModelViewSet):
    # 只统计可显示的文章总数，某标签下有可显示的文章时，该标签才会展示出来
    queryset = Tag.objects.filter(
        visible=v.IS_VISIBLE,
        article__visible=v.IS_VISIBLE,
        article__topic__visible=v.IS_VISIBLE
    ).annotate(
        total=Count('article')
    ).filter(total__gt=0).order_by('id')

    serializer_class = TagSerializer
    pagination_class = BigPagination

    def get_queryset(self):
        article_id = self.request.query_params.get('article', None)

        qs = self.queryset
        if article_id:
            article_id = int(article_id)
            qs = self.queryset.filter(article=article_id)

        return qs


class ArticleAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.visible().order_by('-id')
    serializer_class = ArticleSerializer
    pagination_class = SmallPagination

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

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        article['text'] = md.convert(article['text'])
        article['toc'] = md.toc  # 目录

        _next = instance.get_next()
        _pre = instance.get_pre()
        article['next'] = SmallArticleSerializer(_next).data if _next else None
        article['pre'] = SmallArticleSerializer(_pre).data if _pre else None
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


class ArchiveAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.visible().order_by('-id')
    serializer_class = SmallArticleSerializer

    def get_queryset(self):
        topic_id = self.request.query_params.get('topic', None)

        qs = self.queryset
        if topic_id:
            topic_id = int(topic_id)
            qs = self.queryset.filter(topic=topic_id)

        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        archives = dict()
        for article in queryset:
            year = str(article.ctime.year)
            if year not in archives:
                archives[year] = list()

            archives[year].append(article)

        sort = OrderedDict(sorted(archives.items(), key=lambda t: t[0], reverse=True))
        results = list()
        for year, articleList in sort.items():
            articles = {
                'year': year,
                'total': len(articleList),
                'articles': SmallArticleSerializer(articleList, many=True).data
            }
            results.append(articles)

        resp = {
            'count': len(queryset),
            'data': results
        }
        return Response(resp)


class AboutAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.filter(slug='about-this-blog')
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        instance = self.queryset[0] if self.queryset else None
        serializer = self.get_serializer(instance)
        article = serializer.data
        if not article:
            return Response({})

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        article['text'] = md.convert(article['text'])
        article['toc'] = md.toc  # 目录
        return Response(article)
