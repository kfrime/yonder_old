# -*- coding:utf-8 -*-

from django.urls import path, include
from rest_framework import routers
from . import views

api_router = routers.DefaultRouter()
api_router.register(r'topics', views.TopicAPIView, base_name='api_topics')
api_router.register(r'tags', views.TagAPIView, base_name='api_tags')

urlpatterns = [
    path('api/', include(api_router.urls)),
]
