from django.contrib import admin
from .models import Article, Comment, Artist

admin.site.register(Artist)
admin.site.register(Comment)
admin.site.register(Article)
