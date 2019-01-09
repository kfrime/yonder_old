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
        fields = ('id', 'name', 'slug')


class TagSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()

    class Meta:
        model = Tag
        fields = '__all__'


class SimpleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', )


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    topic = SimpleTopicSerializer()
    # ctime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    ctime = serializers.DateTimeField(format="%Y-%m-%d")
    utime = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Article
        exclude = ('visible', )


class SimpleArticleSerializer(ArticleSerializer):
    """用于展示文章列表，所以不用序列化文章内容"""
    class Meta:
        model = Article
        exclude = ('text', 'visible', )


class SmallArticleSerializer(serializers.ModelSerializer):
    """用于展示文章列表，所以不用序列化文章内容"""
    date = serializers.DateTimeField(source='ctime', format="%m-%d")

    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'date')
