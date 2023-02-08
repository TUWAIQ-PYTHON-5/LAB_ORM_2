from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Blog


def home(request:HttpRequest):
    return render(request,'blog/base.html')


def add_blog(request:HttpRequest):
    if request.method == "POST":
       new_blog=Blog(Title=request.POST["Title"],Content=request.POST["Content"],is_published = request.POST["is_published"])
       new_blog.save()
       return redirect('blog:latest_blog_page')

    return render(request, "blog/add_blog.html")

def latest_blog(request : HttpRequest):

    latest_blog = Blog.objects.all()

    context = {"latest_blog" : latest_blog}
    return render(request, "blog/index.html", context)


def blog_detail(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    return render(request, "blog/blog_detail.html", {"blog" : blog})

def update_blog(request : HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    blog.publish_date = blog.publish_date.isoformat 
    if request.method == "POST":
        blog.title = request.POST["Title"]
        blog.Content = request.POST["Content"]
        blog.is_published = request.POST["is_published"]
        

        blog.save()
        return redirect("blog:latest_blog_page")

    return render(request, "blog/update_blog.html", {"blog" : blog})
def delete_blog(request : HttpRequest, blog_id):
    blog= Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect("blog:latest_blog_page")
def search_blog(request:HttpRequest):
     if request.method=="POST":
        searched= request.POST['searched'] 
        search_blog=Blog.objects.filter(Title__contains=searched)

        return render(request, "blog/search.html", {'searched':searched,'search_blog':search_blog})
     else:
        return render(request, "blog/search.html", {})
 
