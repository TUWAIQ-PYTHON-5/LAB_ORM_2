from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post



def index(request: HttpRequest):

    posts = Post.objects.all()
    context = {"posts" : posts}
    
    return render(request, "main/index.html", context)


def add_post(request : HttpRequest):
    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"])
        new_post.save()

        return redirect("main:index_page")

    return render(request, "main/add_post.html")


def update_blogs(request : HttpRequest, blog_id):

    blog = Post.objects.get(id=blog_id)
    blog.publish_date = blog.publish_date.isoformat 
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published"]
        blog.publish_date = request.POST["publish_date"]
        blog.save()

        return redirect("main:index_page")

    return render(request, "main/update_blog.html", {"blog" : blog})


def blog_detail(request : HttpRequest, blog_id):

    blog = Post.objects.get(id=blog_id)

    return render(request, "main/blog_detail.html", {"blog" : blog})


def delete_blog(request : HttpRequest, blog_id):

    blog = Post.objects.get(id=blog_id)
    blog.delete()
    return redirect("main:index_page")





def search(request : HttpRequest):
    display = int(request.GET.get("dispaly", 10  ))

    search1 = Post.objects.filter(name="")

    context = {"search" : search}
    return render(request, "games/top_games.html", context)



def search_blog(request : HttpRequest):
    if request.method == "POST":
        search = request.POST['search']
        search_blog = Post.objects.filter(title__contains=search)

        return render(request, "main/search.html", {'search_blog':search_blog}) 
    else:
        return render(request, "main/search.html", {})


