from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Blog

def update_blog(request:HttpRequest,blog_id):
    blog= Blog.objects.get(id=blog_id)
    blog.publish_date = blog.publish_date.isoformat #to make it compatible with input value in html
    if request.method == "POST":
        blog.Title = request.POST["Title"]
        blog.Content= request.POST["Content"]
        blog.is_published = request.POST["is_publishe"]
        blog.publish_date = request.POST["publish_date"]

        blog.save()
        return redirect("blog:read_blog_page")

    return render(request, "blog/update_blog.html", {"blog" : blog})



def home(request:HttpRequest):
    return render(request,'blog/base.html')


def add_blog(request:HttpRequest):
    if request.method == "POST":
       new_blog=Blog(Title=request.POST["Title"],Content=request.POST["Content"],is_published = request.POST["is_published"])
       new_blog.save()
       return redirect('blog:read_blog_page')

    return render(request, "blog/add_blog.html")
def update_blog(request:HttpRequest,blog_id):
    blog= Blog.objects.get(id=blog_id)
    blog.publish_date = blog.publish_date.isoformat
    if request.method == "POST":
        blog.Title = request.POST["Title"]
        blog.Content= request.POST["Content"]
        blog.is_published = request.POST["is_publishe"]
        blog.publish_date = request.POST["publish_date"]

        blog.save()
        return redirect("blog:add_blog_page")

    return render(request, "blog/update_blog.html", {"blog" : blog})
def delete_blog(request : HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect("blog:read_blog_page")
def read_blog(request:HttpRequest):
    read_blog = Blog.objects.all()

    context = {"read_blog" :read_blog}
    return render(request,"blog/index.html", context)


def blog_detail(request : HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    return render(request, "blog/blog_detail.html", {"blog" : blog})
def search_title(request:HttpRequest):
    if request.method=="POST":
        search_title=request.POST['search_title']
        searches=Blog.objects.filter(Title__contains=search_title)
        context = {"search_title" : search_title,
                   "searches":searches}
        return render(request, "blog/search_blog.html", context)
    else:

       return render(request, "blog/search_blog.html", context)





