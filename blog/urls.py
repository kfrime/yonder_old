# -*- coding:utf-8 -*-

from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path('article/<int:id>', views.article_detail, name='article_detail'),
    path('article', views.article_list, name='article_list'),
]

