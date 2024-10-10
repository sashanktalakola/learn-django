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