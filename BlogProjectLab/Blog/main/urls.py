from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index_page"),
    path("posts/add/", views.add_post, name="add_post"),
    path("update/<blog_id>/",views.update_blog,name="update_blog"),
    path("details/<plog_id>/", views.plog_detail, name="plog_detail"),

]