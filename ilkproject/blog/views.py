from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Blog, Category


# Create your views here.
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True),
        "categories":Category.objects.all()
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories":Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")


def blog_details(request, slugdata): # slugdata --> from urls.py
    blog = Blog.objects.get(slug=slugdata)
    return render(request, "blog/blog-details.html", {
        "blog": blog
    })

