# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    class Meta:
        db_table = 'News'
    cardimg = models.ImageField(upload_to='news/', blank=True, null=True)
    cardtitle = models.CharField(max_length=200)
    cardtext = models.TextField()
    carddescription = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def datepublished(self):
        return self.created.strftime('%B %d  %I %P ')

    def __str__(self):
        return self.cardtitle

class Newsinline(models.Model):
    class Meta:
        ordering = ('-time',)

    indexes = [
        models.Index(fields=['time']),
    ]
    verbose_name = 'News'
    verbose_name_plural = 'News'
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    text = models.TextField(max_length=400)

    def str(self):
        return self.title
class Comment(models.Model):
    news = models.ForeignKey(News)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    creator = models.TextField()
    class Meta:
        ordering = ('-created',)



