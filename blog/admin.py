# coding: utf-8

from django.contrib import admin
from .models import Post

admin.site.site_header = 'Суперсайт бизнес-инкубатора ВШЭ'
admin.site.site_title = 'Суперсайт бизнес-инкубатора ВШЭ'
admin.site.index_title = 'Суперсайт бизнес-инкубатора ВШЭ'

admin.site.register(Post)
