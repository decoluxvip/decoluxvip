from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Blog

data = {
    "blogs": [
        {
            "id": 1,
            "title": "Nağıllar",
            "image": "1.png",
            "is_active": True,
            "is_home": True,
            "description": "Azərbaycan nağılları"
        },
        {
            "id": 2,
            "title": "Bədii ədəbiyyat",
            "image": "2.png",
            "is_active": True,
            "is_home": True,
            "description": "Bədii ədəbiyyat"
        },
        {
            "id": 3,
            "title": "Xarici ədəbiyyat",
            "image": "3.png",
            "is_active": True,
            "is_home": False,
            "description": "Xarici"
        },
        {
            "id": 4,
            "title": "Dedektiv",
            "image": "4.png",
            "is_active": False,
            "is_home": True,
            "description": "Dedektiv janr"
        },
    ]
}


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
