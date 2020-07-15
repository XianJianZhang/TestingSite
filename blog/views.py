from django.shortcuts import render

# Create your views here.
posts = [
  {"name":"Andy", "date":"2/23/2020", "title":"Shocking news"},
  {"name":"Andy", "date":"2/23/2020", "title":"Shocking news"}
]

def home(request):
  context = {"posts": posts,
             "title": "Home page",
             }
  return render(request, "blog/home.html", context)

def about(request):
  context = {"title":"About page",
             }
  return render(request, "blog/about.html", context)