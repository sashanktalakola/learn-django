from django.contrib import admin
from .models import Category, Tag, Post
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)