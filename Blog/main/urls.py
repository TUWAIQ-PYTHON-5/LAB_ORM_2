from django.urls import path
from . import views

app_name = "main"

urlpatterns = [ #<blog_id> represent object's id changes depends on which blog I clicked | as a hard code we can use it like details/1
    path("", views.index, name="index_page"),
    path("posts/add/", views.add_post, name="add_post"),
    path("light/", views.light, name="light_mode"),
    path("dark/", views.dark, name="dark_mode"),
    path("details/<blog_id>/", views.blog_details, name="details_page"),
    path("update/<blog_id>/", views.update, name="update_page"),
    path("delete/<blog_id>", views.delete_blog, name="delete_page"),
    path("search/", views.search, name="search_page")

]