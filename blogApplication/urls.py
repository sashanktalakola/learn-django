from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("@<str:username>/", views.author, name="author-page"),
    path("@<str:username>/<slug:slug>/", views.viewPost, name="post-page")
]