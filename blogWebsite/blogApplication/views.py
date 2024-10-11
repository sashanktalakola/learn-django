from django.shortcuts import render
from django.conf import settings
import json

# Create your views here.
def index(request):

    dataPath = f"{settings.BASE_DIR}/data/index.json"

    with open(dataPath) as f:
        pageData = json.load(f)
    
    featuredArticlesData = pageData["featured-articles"]
    allArticlesData = pageData["all-articles"]

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
    return render(request, "blogApplication/post.html")