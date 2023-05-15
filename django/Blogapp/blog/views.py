from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog 

data = {
    "blogs" : [
        {
            "id": 1,
            "title": "Full Web",
            "image": "indir.jpeg",
            "is_active": True,
            "is_home": False,
            "description" : "güzel kurs"
        },
        {
            "id": 2,
            "title": "Python",
            "image": "indir.jpeg",
            "is_active": True,
            "is_home": True,
            "description" : "güzel kurs"
        },
        {
            "id": 3,
            "title": "django",
            "image": "prog.jpeg",
            "is_active": False,
            "is_home": True,
            "description" : "güzel kurs"
        },
    ]
}

# Create your views here.
def index(request):
    context = {
        "blogs" : Blog.objects.filter(is_home=True,is_active=True)
    }
    return render(request,"blog/index.html",context)

def blogs(request):
    context = {
        "blogs" : Blog.objects.filter(is_active=True)
    }
    return render(request,"blog/blogs.html",context)

def blogs_details(request,id):
    blog = Blog.objects.get(id=id)
    return render(request,"blog/blogs-details.html",{"blog": blog })