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
        new_post = Post(title=request.POST["title"], content= request.POST["content"], is_published= request.POST["is_published"])
        new_post.save()
        return redirect("main:index_page")

    return render(request, "main/add_post.html")



def detail(request:HttpRequest , blog_id):
    blog_id_content = Post.objects.get(id=blog_id)
    context = {"blog_id_content": blog_id_content}
    return render(request, "main/changes.html", context)

def update(request:HttpRequest, blog_id):
    blog_id_content = Post.objects.get(id=blog_id)
    context = {"blog_id_content": blog_id_content}
    return render(request, "main/add_post.html", context)

def delete(request:HttpRequest, blog_id):
    blog_id_content = Post.objects.filter(id=blog_id).delete()
    context = {"blog_id_content": blog_id_content}
    return render(request, "main/changes.html", context)