from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("", views.home, name="home page"),
    path("new/posts", views.add_post, name="new post" ),
    path("latest/blogs", views.latest_blog, name="latest blogs" ),
    path("details/<blog_id>/", views.detailes, name="blog details" ),
    path("update/<blog_id>/", views.update_blog, name="update_blog" ),
    path("delete/<blog_id>/", views.delete_blog, name="delete_blog" ),
    path("search/", views.search, name="search" )
]