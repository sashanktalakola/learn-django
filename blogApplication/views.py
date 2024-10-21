from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import Post, User, PostContent
import json

# Create your views here.
def index(request):

    posts = Post.objects.all()[:10]

    featuredArticlesData = posts[:4]
    allArticlesData = posts[4:]


    return render(request, "blogApplication/index.html", {
        "featuredArticles": featuredArticlesData,
        "allArticles": allArticlesData
    })

def author(request, username):

    authorData = get_object_or_404(User, username=username)
    authorArticles = Post.objects.filter(user__username=username)[:3]

    return render(request, "blogApplication/author.html", {
        "authorData": authorData,
        "authorArticles": authorArticles
    })

def viewPost(request, username, slug):

    postData = get_object_or_404(Post, user__username=username, slug=slug)
    postContent = PostContent.objects.filter(post=postData)
    postTags = postData.tags.all()
    userPosts = Post.objects.filter(user__username=username).all()[:3]


    return render(request, "blogApplication/post.html", {
        "pageData": postData,
        "postContent": postContent,
        "postTags": postTags,
        "userPosts": userPosts
        
    })