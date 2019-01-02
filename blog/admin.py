# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import (Tag, Topic, Article,)

# Register your models here.
admin.site.register(Tag)
admin.site.register(Topic)
admin.site.register(Article)
