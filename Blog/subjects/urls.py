from django.urls import path
from . import views

app_name = 'subjects'

urlpatterns = [
    
    path('',views.home_page , name="home_page"),
    path('read/',views.read_page,name="read_page"),
    path('write/',views.write_page,name="write_page"),
    path('about/',views.about_page,name="about_page"),
    path('details/<subject_id>/',views.details_page,name="details_page"),
    path('updated/<subject_id>/',views.update_page,name="update_page"),
    path('delete/<subject_id>/',views.delete_page,name="delete_page"),


]