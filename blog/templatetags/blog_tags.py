# -*- coding: utf-8 -*-


from django import template

from ..models import (Tag, Topic, Article)

import request

register = template.Library()


@register.simple_tag
def get_tag_list():
    """ 返回有文章的标签列表"""
    # tags = Tag.objects.exclude(article=None)
    tags = Tag.objects.all()
    return tags


@register.simple_tag
def get_topic_list():
    """ 返回有文章的分类列表"""
    topics = Topic.objects.exclude(article=None)
    return topics


@register.inclusion_tag('article_list.html')
def get_article_list(articles):
    """ 返回文章列表 """
    return {'articles': articles}



