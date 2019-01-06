# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

from utils.const import c_visible as v


class ArticleVisibleManager(models.Manager):
    """Adding extra Manager methods"""

    def visible(self):
        """
        如果某主题/标签不可见，则其下的文章也不可见
        文章可显示：其本身，其主题，其关联的标签都要是可见的
        """
        qs = super().get_queryset().filter(
            visible=v.IS_VISIBLE,
            topic__visible=v.IS_VISIBLE
        ).exclude(
            tags__visible=v.NOT_VISIBLE     # 多对多关系的数据会有重复
        )

        return qs


class Tag(models.Model):
    """
    文章的标签
    """
    _VISIBLE = (
        (v.NOT_VISIBLE, '不可见'),
        (v.IS_VISIBLE, '可见'),
    )
    name = models.CharField('文章标签', max_length=20)
    slug = models.SlugField(unique=True)
    desc = models.TextField('描述', max_length=255, default='')
    visible = models.SmallIntegerField('博客列表中是否可见', default=v.NOT_VISIBLE, choices=_VISIBLE)

    class Meta:
        verbose_name = '标签'

    def __str__(self):
        return self.name


class Topic(MPTTModel):
    """
    文章分类、主题
    """
    _VISIBLE = (
        (v.NOT_VISIBLE, '不可见'),
        (v.IS_VISIBLE, '可见'),
    )
    name = models.CharField('文章分类', max_length=20)
    slug = models.SlugField(unique=True)
    desc = models.TextField('此分类的描述', max_length=256, default='')
    visible = models.SmallIntegerField('博客列表中是否可见', default=v.NOT_VISIBLE, choices=_VISIBLE)

    # 用于构建多级分类树
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',
                            on_delete=models.CASCADE, db_index=True)

    class Meta:
        verbose_name = '分类'

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    文章内容
    """
    _VISIBLE = (
        (v.NOT_VISIBLE, '不可见'),
        (v.IS_VISIBLE, '可见'),
    )
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    title = models.CharField(max_length=150, verbose_name='文章标题')
    summary = models.TextField('文章摘要', max_length=256,
                               default='文章摘要将显示在首页，必填')
    slug = models.SlugField(unique=True)
    text = models.TextField(verbose_name='文章内容')
    ctime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    utime = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    visible = models.SmallIntegerField('博客列表中是否可见', default=v.NOT_VISIBLE, choices=_VISIBLE)

    # 文章和主题是多对一的关系
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING,  verbose_name='文章分类')

    # 文章和标签是多对多的关系
    tags = models.ManyToManyField(Tag, verbose_name='文章标签')

    # 替换原来的objects
    objects = ArticleVisibleManager()

    class Meta:
        verbose_name = '文章'
        ordering = ['-ctime']
        indexes = [
            models.Index(fields=['slug'])
        ]

    def __str__(self):
        # 显示前20个字符和省略号
        s = self.title if len(self.title) < 20 else self.title[:20] + ' ...'
        return s

    def get_pre(self):
        _pre = Article.objects.visible().filter(id__lt=self.id).order_by('-id').first()
        return _pre

    def get_next(self):
        _next = Article.objects.visible().filter(id__gt=self.id).order_by('id').first()
        return _next


