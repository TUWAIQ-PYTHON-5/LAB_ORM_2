from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index_page"),
    path("add/", views.add_post, name="add_post"),
    path("update/<Post_id>/", views.update_post, name="update_post"),
    path("delete/<Post_id>/", views.delete_post, name="delete_post"),
    path("latest/", views.latest_posts, name="latest_posts_page" ),
    path("top/", views.top_posts, name="top_posts_page" ),
    path("detail/<Post_id>/", views.post_detail, name="post_detail"),
]









