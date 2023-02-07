from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.

def main_page(request : HttpRequest):
    
    return render(request, 'main/index.html')

def themeSetDark(request : HttpRequest):
    response = redirect("main:main_page")
    response.set_cookie("theme","Dark", max_age=60*60*24*7)
    return response

def themeSetLight(request : HttpRequest):
    response = redirect("main:main_page")
    response.set_cookie("theme","Light", max_age=60*60*24*7)

    return response