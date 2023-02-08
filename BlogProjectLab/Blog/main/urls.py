from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index_page"),
    path("posts/add/", views.add_post, name="add_post"),
    path("posts/detail/<blog_id>/", views.detail, name="detail_post"),
    path("posts/update/<blog_id>/", views.update, name="update_post"),
    path("posts/detail/<blog_id>/", views.detail, name="detail_post"),

]