# -*- coding: utf-8 -*-

import os
from collections import OrderedDict
import markdown
from django.db.models.aggregates import (Count, Q)
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
            ('data', data)
        ]))


class BigPagination(SmallPagination):
    page_size = 200


class TopicAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.exclude(
        visible=v.NOT_VISIBLE
    ).exclude(
        article__visible=v.NOT_VISIBLE
    ).annotate(
        total=Count('article')
    ).filter(
        total__gt=0
    ).order_by('id')

    serializer_class = TopicSerializer
    pagination_class = BigPagination


class TagAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.exclude(
        visible=v.NOT_VISIBLE
    ).exclude(
        article__visible=v.NOT_VISIBLE
    ).annotate(
        total=Count('article')
    ).filter(
        total__gt=0
    ).order_by('id')
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
    queryset = Article.objects.exclude(
        topic__visible=v.NOT_VISIBLE
    ).exclude(
        tags__visible=v.NOT_VISIBLE
    ).order_by('-id')
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
            # TocExtension(slugify=slugify),
        ])
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



