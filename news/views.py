# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from news.models import  News
from news.models import Newsinline


def home(request):
    news = News.objects.all()
    return render(request, 'main.html', {'news': news})

def newsinline(request):
    Linenews = Newsinline.objects.all()
    return render(request, 'Satia.html', {'news': Linenews})

def statia(request, news_id):
    statia_news = News.objects.get(id=news_id)
    return render(request,'Statia.html',{'news': statia_news})

def sport(request):
    return render(request,'Sport.html',{'news' : News.objects.all()})