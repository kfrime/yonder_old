# -*- coding: utf-8 -*-


from django import template
from django.db.models.aggregates import Count

from ..models import (Tag, Topic, Article)


register = template.Library()


@register.simple_tag
def get_tag_list():
    """ 返回有文章的标签列表"""
    tags = Tag.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)
    return tags


@register.simple_tag
def get_topic_list():
    """ 返回有文章的分类列表"""
    topics = Topic.objects.annotate(total_num=Count('article')).filter(total_num__gt=0)
    return topics


@register.inclusion_tag('article_list.html')
def get_article_list(articles):
    """ 返回文章列表 """
    return {'articles': articles}


@register.inclusion_tag('pagination.html', takes_context=True)
def load_pages(context):
    """ 分页标签模板 """
    return context

