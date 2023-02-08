from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index_page"),
    path("posts/add/", views.post_detail, name="post_detail"),
    path("update/<blog_id>/", views.update_blog, name="update_blog"),
    path("delete/<blog_id>/", views.delete_blog, name="delete_blog"),
    path("latest/", views.latest_blog, name="latest_blog_page" ),
    path("details/<blog_id>/", views.blog_detail, name="blog_detail"),
    path("search/", views.search_blog, name="search_blog"),

]