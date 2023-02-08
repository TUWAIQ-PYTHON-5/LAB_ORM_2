from django.urls import path
from . import views
app_name='blog'

urlpatterns = [
    path('add/', views.add_blog, name='add_blog_page'),
    path('update_blog/<blog_id>/', views.update_blog,name="update_page"),
    path('',views.home,name='home_page'),
    path("delete/<blog_id>/", views.delete_blog, name="delete_blog"),
    path('read/',views.read_blog,name='read_blog_page'),
    path("details/<blog_id>/", views.blog_detail, name="blog_detail"),
    path('search/',views.search_title,name="search_page"),
    
   

]