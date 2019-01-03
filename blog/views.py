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


class TopicAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.exclude(visible=v.NOT_VISIBLE).order_by('id')
    serializer_class = TopicSerializer
    # pagination_class = BigPagination

    def get_queryset(self):
        return Topic.objects.annotate(total=Count('article')).filter(total__gt=0)

