# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from news.models import News, Sport, Cultura, Country
from news.models import Newsinline

admin.site.register(News)
admin.site.register(Newsinline)
admin.site.register(Sport)
admin.site.register(Cultura)
admin.site.register(Country)
