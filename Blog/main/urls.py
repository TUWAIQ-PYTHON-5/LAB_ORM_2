from django.urls import path
from . import views

app_name = "main"


urlpatterns = [

    path('', views.home_page, name="home_page"),
    path("update/<post_id>/", views.update_post, name="update_post"), 
    path("delete/<post_id>/", views.delete_post, name="delete_post"),
    path("details/<post_id>/", views.post_detail, name="post_detail"),
    path("search/", views.post_search, name="post_search"),    


   
]