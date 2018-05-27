# -*- coding:utf-8 -*-
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Tag(models.Model):
    """
    文章的标签
    """
    name = models.CharField('文章标签', max_length=20)
    slug = models.SlugField(unique=True)
    desc = models.TextField('描述', max_length=255, default='')

    class Meta:
        verbose_name = '标签'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """ 查看该标签下的所有文章列表 """
        pass


class Topic(MPTTModel):
    """
    文章分类、主题
    """
    name = models.CharField('文章分类', max_length=20)
    slug = models.SlugField(unique=True)
    desc = models.TextField('此分类的描述', max_length=256, default='')

    # 用于构建多级分类树
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',
                            on_delete=models.CASCADE, db_index=True)

    class Meta:
        verbose_name = '分类'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """ 查看该分类下的所有文章列表 """
        return reverse('blog:topic', kwargs={'id': self.id})


class Article(models.Model):
    """
    文章内容
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    title = models.CharField(max_length=150, verbose_name='文章标题')
    summary = models.TextField('文章摘要', max_length=256,
                               default='文章摘要将显示在首页，必须填写...')
    text = models.TextField(verbose_name='文章内容')
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    slug = models.SlugField(unique=True)

    # 文章和主题是多对一的关系
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='文章分类')

    # 文章和标签是多对多的关系
    tags = models.ManyToManyField(Tag, verbose_name='文章标签')

    class Meta:
        verbose_name = '文章'
        ordering = ['-created']

    def __str__(self):
        # 显示前20个字符和省略号
        s = self.title[:20]
        return s if len(self.title) < 20 else s + ' ...'

    def get_absolute_url(self):
        """ 查看该文章的具体内容 """
        return reverse('blog:detail', kwargs={'id': self.id})






