# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .models import (Tag, Topic, Article)

# Create your views here.


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {
        'tags': Tag.objects.all(),
        'topics': Topic.objects.all().exclude(parent=None),
        'articles': Article.objects.all(),
    }
    return render(request, 'index.html', context=context)

