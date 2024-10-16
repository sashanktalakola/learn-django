from django.contrib import admin
from .models import Category, Tag, Post, User


# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)