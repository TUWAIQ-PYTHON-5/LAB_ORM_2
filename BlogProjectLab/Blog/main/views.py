from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.

def index(request : HttpRequest):
    
    posts = Post.objects.all()
    context = {"posts" : posts}

    return render(request, "main/index.html", context)



def add_post(request : HttpRequest):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content= request.POST["content"], is_published= request.POST["is_published"],publish_date= request.POST["publish_date"])
        new_post.save()

        return redirect("main:index_page")

    return render(request, "main/add_post.html")

def update_blog( request:HttpRequest,blog_id):
    blogar=Post.objects.get(id=blog_id)
    if request.method == "POST":
        blogar.title=request.POST["title"]
        blogar.content=request.POST["content"]
        blogar.is_published=request.POST["is_published"]
        blogar.publish_date=request.POST["publish_date"]

        
        blogar.save()
        return redirect("main:latest_blog_page")

    return render(request, "main/update_blog.html", {"blogar" : blogar})

def delete_plog(request : HttpRequest, plog_id):
    blogar = Post.objects.get(id=plog_id)
    blogar.delete()
    return redirect("main:latest_plogar_page")
def top_plog(request : HttpRequest):

    top_plog = Post.objects.filter(titel__gt=4)

    context = {"top_plog" : top_plog}
    return render(request, "main/top_plog.html", context)

def plog_detail(request : HttpRequest, plog_id):

    blogar = Post.objects.get(id=plog_id)



    return render(request, "main/plog_detail.html", {"blogar" :blogar})