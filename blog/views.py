from django.shortcuts import render
from blog.models import Post

def home(request):
  context = {"posts": Post.objects.all(),
             "title": "Home page",
             }
  return render(request, "blog/home.html", context)

def about(request):
  context = {"title":"About page",
             }
  return render(request, "blog/about.html", context)