from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.leatestBlogs, name="leatestBlogs" ),
    path("add/", views.addBlog, name="addBlog"),
    path("leatestBlogs/", views.leatestBlogs, name="leatestBlogs" ),
    path("update/<blog_id>/", views.updateBlog, name="updateBlog"),
    path("details/<blog_id>/", views.blogDetail, name="blogDetail"),
    path("delete/<blog_id>/", views.deleteBlog, name="deleteBlog"),
    path("find/", views.findBlog, name="findBlog" ),

]##