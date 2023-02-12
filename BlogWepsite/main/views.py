from django.shortcuts import render, redirect 
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.views.generic import TemplateView, ListView


# Create your views here.

def index(request : HttpRequest):
    
    posts = Post.objects.all()
    context = {"posts" : posts}

    return render(request, "main/index.html", context)



def post_detail(request : HttpRequest):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content= request.POST["content"], is_published= request.POST["is_published"])
        new_post.save()

        return redirect("main:index_page")

    return render(request, "main/post_detail.html")


def latest_blog(request : HttpRequest):

    display = int(request.GET.get("display", 10))

    latest_blog = Post.objects.all()

    context = {"latest_blog" : latest_blog}
    return render(request, "main/index.html", context)



def update_blog(request : HttpRequest, blog_id):

    blog = Post.objects.get(id=blog_id)
    blog.publish_date = blog.publish_date.isoformat #what ???????
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published"]
        blog.publish_date = request.POST["publish_date"]

        blog.save()
        return redirect("main:latest_blog_page")

    return render(request, "main/update.html", {"main" : blog})



def blog_detail(request : HttpRequest, blog_id):

    blog = Post.objects.get(id=blog_id)

    return render(request, "main/detail.html", {"main" : blog})


def delete_blog(request : HttpRequest, blog_id):
    blog = Post.objects.get(id=blog_id)
    blog.delete()
    return redirect("main:latest_blog_page")



def search(request : HttpRequest):

    search1 = Post.objects.filter(name="")

    context = {"search" : search}
    return render(request, "main/top_games.html", context)



def search_blog(request : HttpRequest):
    if request.method == "POST":
        search = request.POST['search']
        search_blog = Post.objects.filter(title__contains=search)

        return render(request, "main/search.html", {'search_blog':search_blog}) 
    else:
        return render(request, "main/search.html", {})