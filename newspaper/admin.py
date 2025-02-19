from django.contrib import admin

# Register your models here.
from newspaper.models import Category, Comment, NewsLetter, Post, Tag, Profile

admin.site.register([ Tag, Category, Profile, Comment, NewsLetter, ])

from django_summernote.admin import SummernoteModelAdmin
from .models import  Post

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)