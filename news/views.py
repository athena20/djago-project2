# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from news.models import  News
from news.models import Newsinline, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from newssite.forms import BookAddForm


def home(request):
    news = News.objects.all()
    return render(request, 'main.html', {'news': news,})

def lastnews(request):
    Linenews = News.objects.all()
    return render(request, 'Satia.html', {'news': Linenews})

def statia(request, news_id):
    news = get_object_or_404(News, id=news_id)
    comments = Comment.objects.filter(news=news)
    form = BookAddForm((request.POST or None), (request.FILES or None))
    added = False
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.news = news
            comment.save()
            added = True
            return HttpResponseRedirect(reverse('Statia', kwargs={'news_id': news_id}))
    return render(request, 'Statia.html', {'new': news, 'comments': comments, 'form': form, 'added': added})


def sport(request):
    return render(request,'Sport.html',{'news' : News.objects.all()})
def cultura(request):
    return render(request,'Cultura.html',{'news' : News.objects.all()})
def country(request):
    return render(request,'Country.html',{'news' : News.objects.all()})