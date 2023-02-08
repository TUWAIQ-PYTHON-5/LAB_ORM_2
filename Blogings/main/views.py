from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
from datetime import date



def leatestBlogs(request : HttpRequest):
    leatestBlogs = Blog.objects.all()
    context = {"leatestBlogs" : leatestBlogs}
    return render(request, "main/leatestBlogs.html", context)
##################################################################
def addBlog(request : HttpRequest):
    if request.method == "POST":
        newBlog = Blog(title= request.POST["title"], content = request.POST["content"], isPublish = request.POST["isPublish"])
        newBlog.save()
        return redirect("main:leatestBlogs")
    return render(request, "main/addBlog.html")
##################################################################
def updateBlog(request : HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.writingDate = blog.writingDate.isoformat #to make it compatible with input value in html
    if request.method == "POST":
        Blog.title = request.POST["title"]
        Blog.content = request.POST["content"]
        Blog.isPublish = request.POST["isPublish"]
        Blog.writingDate= request.POST["writingDate"]
        blog.save()
        return redirect("main:leatestBlogs")
    return render(request, "main/updateBlog.html", {"blog" : blog})
##################################################################
def blogDetail(request : HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, "main/blogDetail.html", {"blog" : blog})
##################################################################
def deleteBlog(request : HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect("games:latest_games_page")
##################################################################
def findBlog(request : HttpRequest):
    if request.method == "POST":
        toFind = request.POST['toFind']  
        result = Blog.objects.filter(title__contains=toFind)
        return render(request, "main/findBlog.html", {'toFind' : toFind, 'result' : result})
    
    else:
        return render(request, "main/findBlog.html", {'toFind' : toFind})