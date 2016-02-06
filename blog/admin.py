# coding: utf-8

from django.contrib import admin
from .models import Post

admin.site.site_header = 'margoolis'
admin.site.site_title = 'margoolis'
admin.site.index_title = 'margoolis'

admin.site.register(Post)
