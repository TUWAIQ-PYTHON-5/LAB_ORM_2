from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("theme/dark/", views.themeSetDark, name="theme_set_dark"),
    path("theme/light/", views.themeSetLight, name="theme_set_light"),
    
]