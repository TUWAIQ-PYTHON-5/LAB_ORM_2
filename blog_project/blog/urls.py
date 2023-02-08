from django.urls import path
from . import views
app_name='blog'

urlpatterns = [
    path('',views.home,name='home_page'),
    path('add/', views.add_blog, name='add_blog_page'),
    path("latest/", views.latest_blog, name="latest_blog_page"),
    path("details/<blog_id>/", views.blog_detail, name="blog_detail"),
    path("update/<blog_id>/", views.update_blog, name="update_blog"),
    path("delete/<blog_id>/", views.delete_blog, name="delete_blog"),
    path("search/", views.search_blog, name="search_blog"),
    
   

]