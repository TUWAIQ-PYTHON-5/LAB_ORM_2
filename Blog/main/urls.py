from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name="index_page"),
    path('post/add/', views.add_post, name="add_post"),
    path("update/<blog_id>/", views.update_blogs, name="update_blog"),
    path("delete/<blog_id>/", views.delete_blog, name="delete_blog"),
    path("details/<blog_id>/", views.blog_detail, name="blog_detail"),
    path("search/", views.search_blog, name="search_blog"),
]
