from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index_page"),
    path("posts/add/", views.add_post, name="add_post"),
    path('show_Post/<post_id>' , views.post_Details , name='show_post'),
    path('Delete_post/<post_id>' , views.Delete_post , name='Delete_post'),
    path('update_post/<post_id>' , views.updateing_post , name='update_post'),
]

