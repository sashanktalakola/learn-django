from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .utils import getRandomSlug


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            self.slug = getRandomSlug(self.slug, self.user.username)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title