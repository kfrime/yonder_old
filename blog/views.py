# -*- coding:utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.cache import cache
from django.utils.text import slugify

from markdown.extensions.toc import TocExtension  # 锚点的拓展
import markdown

from .models import (Tag, Topic, Article)


class IndexView(generic.ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = 5
    # paginate_orphans = 3

    def get_ordering(self):
        ordering = super(self.__class__, self).get_ordering()
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return ('-views', '-update_date', '-id')
        return ordering


def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)

    update_time = article.update_time.strftime("%Y%m%d%H%M%S")
    md_key = '{}_md_{}'.format(article.id, update_time)
    cache_md = cache.get(md_key)
    if cache_md:
        md = cache_md
    else:
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            # TocExtension(slugify=slugify),
        ])
        cache.set(md_key, md, 60 * 60 * 12)
    article.text = md.convert(article.text)
    article.toc = md.toc    # 目录

    context = {
        'article': article
    }
    return render(request, 'detail.html', context=context)


def article_list(request):
    tag_id = request.GET.get('tag_id', None)
    topic_id = request.GET.get('topic_id', None)
    articles = None
    if tag_id:
        articles = Article.objects.filter(tags=int(tag_id))
    if topic_id:
        articles = Article.objects.filter(topic_id=int(topic_id))

    context = {
        'articles': articles,
    }
    return render(request, 'article_list.html', context=context)


def about(request):
    return render(request, 'about.html')


def topic(request, id):
    topic = get_object_or_404(Topic, pk=id)
    articles = Article.objects.filter(topic=topic)
    context = {
        'topic': topic,
        'articles': articles,
    }
    return render(request, 'topic.html', context=context)


def tag(request, id):
    tag = get_object_or_404(Tag, pk=id)
    articles = Article.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'articles': articles,
    }
    return render(request, 'tag.html', context=context)
