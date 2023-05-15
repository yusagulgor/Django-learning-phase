from django.urls import path
from . import views

#shell
#python manage.py runserver 
#http://127.0.0.1:8000/
urlpatterns =[
    path("", views.index , name="home"),
    path("index", views.index),
    path("blogs", views.blogs,name="blogs"),
    path("blogs/<int:id>", views.blogs_details, name="blogs_details"),
]
