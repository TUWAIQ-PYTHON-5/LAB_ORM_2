from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_page, name="blog_page"),
    path("add/", views.add_blog, name="add_new_blog"),
    path("view/", views.view_blogs, name="view_blogs_page"),
    path("details/<blog_id>/", views.blog_detail, name="blog_detail"),
    path("update/<blog_id>/", views.update_blog, name="update_blog"),
    path("delete/<blog_id>/", views.delete_blog, name="delete_blog"),
    path("search/", views.search_blog, name="search_blog"),
]