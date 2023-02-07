from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("Science/", views.science_page, name="science_page"),
    path("Health/", views.health_page, name="health_page"),
    path("Business/", views.business_page, name="business_page"),
    path("Design/", views.design_page, name="design_page"),
    path("Technology/", views.tech_page, name="tech_page"),
    
]