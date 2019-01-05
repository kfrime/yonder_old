# -*- coding:utf-8 -*-

from django.urls import path, include
from rest_framework import routers
from . import views

api_router = routers.DefaultRouter()
api_router.register(r'topics', views.TopicAPIView, base_name='api_topics')
api_router.register(r'tags', views.TagAPIView, base_name='api_tags')
api_router.register(r'articles', views.ArticleAPIView, base_name='api_articles')
api_router.register(r'archives', views.ArchiveAPIView, base_name='api_archives')

urlpatterns = [
    path('api/', include(api_router.urls)),
]
