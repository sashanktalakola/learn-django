from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import Post
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

    dataPath = f"{settings.BASE_DIR}/data/author.json"

    with open(dataPath) as f:
        pageData = json.load(f)

    authorData = pageData["authorData"]
    authorArticlesData = pageData["authorArticles"]

    return render(request, "blogApplication/author.html", {
        "authorData": authorData,
        "authorArticles": authorArticlesData
    })

def viewPost(request, username, slug):

    postData = get_object_or_404(Post, user__username=username, slug=slug)

    dataPath = f"{settings.BASE_DIR}/data/post.json"

    with open(dataPath) as f:
        pageData = json.load(f)


    return render(request, "blogApplication/post.html", {
        "pageData": pageData,
        
    })