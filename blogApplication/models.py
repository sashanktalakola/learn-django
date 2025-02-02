from django.db import models
from django.utils.text import slugify
from .utils import getRandomSlug


class User(models.Model):
    username = models.CharField(max_length=150, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    profile_picture = models.CharField(max_length=255, blank=True, null=True, default="img/default/user-image/default-user-img.jpg")
    bio = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    short_intro = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)
    time_to_read = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)
            self.slug = getRandomSlug(self.slug, self.user.username)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='contents')
    content = models.TextField()
    content_type = models.CharField(max_length=50)

    def __str__(self):
        return f"Content for {self.post.title} - {self.content_type}"