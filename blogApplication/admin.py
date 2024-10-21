from django.contrib import admin
from .models import Tag, Post, User, PostContent


# Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(PostContent)