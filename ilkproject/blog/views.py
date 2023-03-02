from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def blogs(request):
    return render(request, "blog/blogs.html")


def blog_details(request, id):
    if id < 4:
        z = "salam: "
    else:
        z = "sagol: "
    return render(request, "blog/blog-details.html", {
        "id": z+str(id)
    })
