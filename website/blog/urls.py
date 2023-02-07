from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_page, name="blog_page"),
    path("add/", views.add_blog, name="add_new_blog"),
    path("update/<blog_id>/", views.update_blogs, name="update_blog"),
    path("delete/<blog_id>/", views.delete_blog, name="delete_blog"),
    path("latest/", views.latest_blog, name="latest_blog_page" ),
    path("details/<blog_id>/", views.blog_detail, name="blog_detail"),
    path("search/", views.search, name="search"),


]