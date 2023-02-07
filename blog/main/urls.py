from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('' , views.home_page , name='home_page'),
    path('add/' , views.add_new_blog , name='add_blog'),
    path('ready_to_share/', views.show_only_what_is_ready_for_publish , name='ready_share'),
    path('not_ready_to_share/', views.show_only_what_is_not_ready_for_publish , name='not_ready_share'),
    path('show_all' , views.show_all , name='show_all'),
    path('show_Post/<post_id>' , views.post_Details , name='show_post'),
    path('Delete_post/<post_id>' , views.Delete_post , name='Delete_post'),
    path('update_post/<post_id>' , views.updateing_post , name='update_post'),
    path('search_post/' , views.search_post , name='search_post'),
]