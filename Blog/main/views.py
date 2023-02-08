from django.shortcuts import render,redirect
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

    

def blog_details(request : HttpRequest, blog_id):
    blog = Post.objects.get(id = blog_id)

    return render(request, "main/Blog_details.html", {"blog" : blog})


def update(request : HttpRequest, blog_id):

    blog = Post.objects.get(id=blog_id)
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]

        blog.save()
        return redirect("main:index_page")

    return render(request, "main/update.html", {"blog" : blog})


def delete_blog(request : HttpRequest, blog_id):
    blog = Post.objects.get(id=blog_id)
    blog.delete()
    return redirect("main:index_page")


def search(request : HttpRequest):
    if request.method == "POST":
        searched = request.POST['searched']
        print(searched)
        posts = Post.objects.filter(title__contains = searched)
        return render(request, "main/search_page.html", {"searched" : searched, "posts" : posts})
    else :
        return render(request, "main/search_page.html")




