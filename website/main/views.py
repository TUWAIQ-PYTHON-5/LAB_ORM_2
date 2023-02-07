from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.

def main_page(request : HttpRequest):
    
    return render(request, 'main/index.html')


def health_page (request : HttpRequest):

    return render (request, "main/Health.html")


def science_page (request : HttpRequest):

    return render (request, "main/Science.html")


def business_page (request : HttpRequest):

    return render (request, "main/Business.html")

def design_page (request : HttpRequest):

    return render (request, "main/Design.html")


def tech_page (request : HttpRequest):

    return render (request, "main/Technology.html")
