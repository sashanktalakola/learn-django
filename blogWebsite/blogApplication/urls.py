from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("@<str:username>/", views.author),
    path("@<str:username>/<slug:slug>/", views.viewPost)
]