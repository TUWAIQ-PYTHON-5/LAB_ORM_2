from django.urls import path
from . import views





app_name = "blog"

urlpatterns = [
    path("", views.index, name="blogs_page" ),
    path("blogs/add/", views.add_post, name="add_new_post"),
    path("blogs/details/<post_id>", views.detail_post, name="details_post"),
    path("blogs/update/<post_id>", views.post_update, name="post_update"),
    path("blogs/delete/<post_id>", views.delete_post, name="post_delete"),
    path("blogs/search/", views.search, name="search_post")
]
