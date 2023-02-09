from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.


def home_page (request : HttpRequest):
    posts = Post.objects.all()
    if request.method == "POST":
        new_post = Post(title=request.POST["title"], Content=request.POST["content"], is_published=request.POST["is_published"])
        new_post.save()
        print(request.POST["title"])
        return redirect("main:home_page")
    context = {"posts" : posts}
    return render (request,"main/home.html", context)


def update_post (request : HttpRequest, post_id):
    posts = Post.objects.get(id=post_id)
    posts.publish_date = posts.publish_date.isoformat 
    if request.method == "POST":
        posts.title = request.POST["title"]
        posts.Content = request.POST["content"]
        posts.is_published = request.POST["is_published"]
        posts.publish_date = request.POST["publish_date"]

        posts.save()
        return redirect("main:post_detail")

    return render(request,"main/update_post.html", {"post" : posts})



def delete_post (request : HttpRequest, post_id):
    posts = Post.objects.get(id=post_id)
    posts.delete()
    return redirect("main:home_page")



def post_detail(request : HttpRequest, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, "main/post_detail.html", {"post" : post})



def post_search(request: HttpRequest):
    posts = Post.objects.filter(name__contains=request.GET.get('search'))

    return render(request, 'main/post_detail.html', {'posts':posts})