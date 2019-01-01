# -*- coding:utf-8 -*-

import hashlib
from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Tag(models.Model):
    """
    文章的标签
    """
    name = models.CharField('文章标签', max_length=20)
    slug = models.SlugField(unique=True)
    desc = models.TextField('描述', max_length=255, default='')
    visible = models.BooleanField('博客列表中是否可见', default=False)

    class Meta:
        verbose_name = '标签'

    def __str__(self):
        return self.name


class Topic(MPTTModel):
    """
    文章分类、主题
    """
    name = models.CharField('文章分类', max_length=20)
    slug = models.SlugField(unique=True)
    desc = models.TextField('此分类的描述', max_length=256, default='')
    visible = models.BooleanField('博客列表中是否可见', default=False)

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
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    title = models.CharField(max_length=150, verbose_name='文章标题')
    summary = models.TextField('文章摘要', max_length=256,
                               default='文章摘要将显示在首页，必填')
    slug = models.SlugField(unique=True)
    text = models.TextField(verbose_name='文章内容')
    ctime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    utime = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    visible = models.BooleanField('博客列表中是否可见', default=False)

    # 文章和主题是多对一的关系
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING,  verbose_name='文章分类')

    # 文章和标签是多对多的关系
    tags = models.ManyToManyField(Tag, verbose_name='文章标签')

    class Meta:
        verbose_name = '文章'
        ordering = ['-create_time']
        indexes = [
            models.Index(fields=[''])
        ]

    def __str__(self):
        # 显示前20个字符和省略号
        s = self.title if len(self.title) < 20 else self.title[:20] + ' ...'
        return s

    def get_pre(self):
        return Article.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):
        return Article.objects.filter(id__gt=self.id).order_by('id').first()

    def get_id(self):
        m = hashlib.md5()
        m.update(b"Nobody inspects")
        m.update(b" the spammish repetition")
        m.digest()
        return hashlib.md5.new(self.title, self.slug).digest()

