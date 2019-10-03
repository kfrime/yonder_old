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
    path(r'', views.IndexView.as_view(), name='index'),

    path('article/<int:id>', views.article_detail, name='detail'),
    path('topic/<int:id>', views.topic, name='topic'),
    path('tag/<int:id>', views.tag, name='tag'),

    path('article', views.article_list, name='article_list'),
    path('about', views.about, name='about'),

    path('api/', include(api_router.urls)),
]

