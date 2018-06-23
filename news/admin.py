# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from news.models import News
from news.models import Newsinline

admin.site.register(News)
admin.site.register(Newsinline)