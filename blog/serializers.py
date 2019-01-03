# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (Topic, Tag, Article,)


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='username')

    class Meta:
        model = User
        # fields = ('id', 'username')
        fields = ('name',)


class TopicSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()

    class Meta:
        model = Topic
        fields = ('id', 'name', 'slug', 'desc', 'total')
        # fields = '__all__'


class SimpleTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', )


class TagSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()

    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    topic = SimpleTopicSerializer()
    ctime = serializers.DateTimeField(source='ctime', format="%Y-%m-%d %H:%M:%S")
    utime = serializers.DateTimeField(source='utime', format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Article
        exclude = ('visible', )


class SimpleArticleSerializer(ArticleSerializer):
    """用于展示文章列表，所以不用序列化文章内容"""
    class Meta:
        model = Article
        exclude = ('text', 'visible', )


class SmallArticleSerializer(ArticleSerializer):
    """用于展示文章列表，所以不用序列化文章内容"""
    date = serializers.DateTimeField(source='create_time', format="%m-%d")

    class Meta:
        model = Article
        fields = ('id', 'title', 'date')
