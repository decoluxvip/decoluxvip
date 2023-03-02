from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Homepage")


def blogs(request):
    return HttpResponse("Blogs")


def blog_details(request, id):
    return HttpResponse("Blog_details: " + str(id))
