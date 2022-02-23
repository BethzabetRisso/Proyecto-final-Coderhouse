from urllib import request
from django.shortcuts import render
from blog.models import Post, Categoria
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms


# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request,'blog/blog.html', {"posts": posts})

def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias =categoria)

    return render(request, "blog/categoria.html", {"categoria": categoria,"posts": posts})


# class PostListado(ListView): 
#     model = Post
 
def postDetalle(request, id): 
    post = Post.objects.get(id = id)
    print('estoy aca')
    return render(request,'blog/detalles.html',{'post':post})