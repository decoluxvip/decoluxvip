from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path('category/<slug:slugdata>', views.blog_by_category, name='blog_bu_category'),
    path("blog-details/<slug:slugdata>", views.blog_details, name="blog-details"),
    # <slug:slugdata> --> typeFromDB:nameSlugVariable
]
