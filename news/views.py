# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from news.models import  News
from news.models import Newsinline
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    news = News.objects.all()
    comments = Comment.objects.filter(news=news)
    form = BookAddForm(request.POST or None)
    # paginator
    page = request.GET.get('page')
    paginator = Paginator(comments, 3)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    added = False
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.news = news
            comment.picture = url
            comment.save()
            added = True
            return HttpResponseRedirect(reverse('single_book', kwargs={'book_id': book_id}))
    return render(request, 'main.html', {'news': news, 'comment': comments})

def newsinline(request):
    Linenews = Newsinline.objects.all()
    return render(request, 'Satia.html', {'news': Linenews})

def statia(request, news_id):
    statia_news = News.objects.get(id=news_id)
    return render(request,'Statia.html',{'news': statia_news})