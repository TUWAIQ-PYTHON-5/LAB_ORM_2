from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog



# Create your views here.

def blog_page(request : HttpRequest):
    
    return render(request, 'blog/index.html')


def add_blog(request : HttpRequest):

    if request.method == "POST":
        #to add a new entry
        new_blog = Blog(title= request.POST["title"], content = request.POST["content"], is_published = request.POST["is_published"], publish_date=request.POST["publish_date"])
        new_blog.save()
        return redirect("blog:view_blogs_page")


    return render(request, "blog/add_blog.html")


def view_blogs(request : HttpRequest):

    view_blogs = Blog.objects.all()

    context = {"view_blogs" : view_blogs}
    return render(request, "blog/index.html", context)


def update_blog(request : HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    blog.publish_date = blog.publish_date.isoformat #to make it compatible with input value in html
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published"]
        blog.publish_date = request.POST["publish_date"]

        blog.save()
        return redirect("blog:view_blogs_page")

    return render(request, "blog/update_blog.html", {"blog" : blog})

def delete_blog(request : HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect("blog:view_blogs_page")

def blog_detail(request : HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)

    return render(request, "blog/blog_detail.html", {"blog" : blog})

def search_blog(request : HttpRequest):
    if request.method == "POST":
        search = request.POST['search']
        search_blog = Blog.objects.filter(title__contains=search)

        return render(request, "blog/search_blog.html", {'search_blog':search_blog}) 
    else:
        return render(request, "blog/search_blog.html", {})