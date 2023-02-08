from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index_page"),
    path("posts/add/", views.add_post, name="add_post"),
    path("details/<blog_id>/", views.blog_details, name="details_page"),
    path("update/<blog_id>/", views.update, name="update_page"),
    path("delete/<blog_id>", views.delete_blog, name="delete_page"),
    path("search/", views.search, name="search_page")
]