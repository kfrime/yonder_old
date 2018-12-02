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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class SimpleTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', )


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    # author_name = serializers.CharField(source='author.username')
    topic = SimpleTopicSerializer()
    # tags = TagSerializer()
    ctime = serializers.DateTimeField(source='create_time', format="%Y-%m-%d %H:%M:%S")
    utime = serializers.DateTimeField(source='update_time', format="%Y-%m-%d %H:%M:%S")
    # tags = TagSerializer()

    class Meta:
        model = Article
        exclude = ('create_time', 'update_time')


class SimpleArticleSerializer(ArticleSerializer):
    class Meta:
        model = Article
        exclude = ('text', 'create_time', 'update_time')
