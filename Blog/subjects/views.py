from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpRequest
from .models import Subject


def home_page(request : HttpRequest):
    return render(request,"subjects/home_page.html")


def write_page(request : HttpRequest):

    if request.method == "POST":
        new_subject = Subject(title= request.POST["title"], content = request.POST["content"], is_published = request.POST["is_published"], published_date=request.POST["published_date"])
        new_subject.save()
        return redirect("subjects:read_page")

    return render(request,"subjects/write.html")
    

def read_page(request :HttpRequest):
    
    subjects_save = Subject.objects.all()
    context = {"subjects_save" : subjects_save}
    return render(request,"subjects/read.html", context)
    


def details_page(request : HttpRequest,subject_id):
    subject = Subject.objects.get(id=subject_id)
    return render(request,"subjects/subject_details.html", {"subject" : subject})



def update_page(request : HttpRequest,subject_id):

    subject = Subject.objects.get(id=subject_id)
    
    if request.method == "POST":

        subject.title = request.POST["title"]
        subject.content = request.POST["content"]
        subject.is_published = request.POST["is_published"]
        
        subject.save()
        return redirect("subjects:read_page")

    return render(request,"subjects/update_subject.html", {"subject" : subject})

def delete_page(request : HttpRequest, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject.delete()
    return redirect("subjects:read_page")
    
def search_page(request : HttpRequest):

    if request.method == "POST":
        search = request.POST.get("search")
        result_search = Subject.objects.filter(title__icontains=search)
        
        return render(request,"subjects/subject_details.html", {"result_search" : result_search})



    

def about_page(request : HttpRequest):
    return render(request,"subjects/about.html")


