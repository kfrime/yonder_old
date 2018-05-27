# -*- coding:utf-8 -*-

from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path('article/<int:id>', views.article_detail, name='detail'),
    path('topic/<int:id>', views.topic, name='topic'),

    path('article', views.article_list, name='article_list'),
    path('about', views.about, name='about'),
]

