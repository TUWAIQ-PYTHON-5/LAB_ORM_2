from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post , Review

# Create your views here.

def index(request : HttpRequest):
    Posts = Post.objects.all()
    context = {"Posts" : Posts}
    return render(request, "main/index.html", context)



def add_post(request : HttpRequest):
    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content= request.POST["content"], is_published= request.POST["is_published"])
        new_post.save()
        return redirect("main:index_page")
    return render(request, "main/add_post.html")




def update_post(request : HttpRequest, Post_id):
    post = Post.objects.get(id=Post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.is_published = request.POST["is_published"]
        post.publish_date = request.POST["publish_date"]
        post.save()
        return redirect("main:latest_blogs_page")
    return render(request, "main/update_post.html", {"Posts" : post})



def delete_post(request : HttpRequest, Post_id):
    Posts = Post.objects.get(id=Post_id)
    Posts.delete()
    return redirect("main:index_page")
    

def latest_posts(request : HttpRequest):
    display = int(request.GET.get("display", 10))
    if 'search' in request.GET:
        latest_posts = Post.objects.filter(title__contains=request.GET['search']).order_by()
    else:
      latest_posts = Post.objects.all().order_by('-title')
    context = {"latest_posts" : latest_posts}
    return render(request, "main/index.html", context , {"Post" : latest_posts})


def top_posts(request : HttpRequest):
    top_posts = Post.objects.filter() ###
    context = {"top_posts" : top_posts}
    return render(request, "main/top_posts.html", context)


def post_detail(request : HttpRequest, Post_id):
    Posts = Post.objects.get(id=Post_id)
    return render(request, "main/post_detail.html", {"Posts" : Posts})





