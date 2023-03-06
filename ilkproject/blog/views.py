from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Blog


# Create your views here.
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True)
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True)
    }
    return render(request, "blog/blogs.html", context)


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")


def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    # blogs = data["blogs"]
    # selectedBlog = [blog for blog in blogs if blog["id"] == id][0]
    return render(request, "blog/blog-details.html", {
        "blog": blog
    })
