# -*- coding: utf-8 -*-

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
    queryset = Topic.objects.exclude(visible=v.NOT_VISIBLE).order_by('id')
    serializer_class = TopicSerializer
    pagination_class = BigPagination

    def get_queryset(self):
        return Topic.objects.annotate(total=Count('article')).filter(total__gt=0)


class TagAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.exclude(article__isnull=True).annotate(total=Count('article')).order_by('id')
    serializer_class = TagSerializer
    pagination_class = BigPagination

    def get_queryset(self):
        article_id = self.request.query_params.get('article', None)

        qs = self.queryset
        if article_id:
            article_id = int(article_id)
            qs = self.queryset.filter(article=article_id)

        return qs



