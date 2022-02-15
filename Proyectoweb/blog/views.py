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
 
class PostDetalle(DetailView): 
    model = Post
 
class PostCrear(SuccessMessageMixin, CreateView): 
    model = Post
    form = Post
    fields = "__all__" 
    success_message = 'Post Creado Correctamente !'    
 
    
    def get_success_url(self):        
        return reverse('posts') 
 
class PostActualizar(SuccessMessageMixin, UpdateView): 
    model = Post
    form = Post
    fields = "__all__"  
    success_message = 'Postre Actualizado Correctamente !'  
 

    def get_success_url(self):               
        return reverse('posts') 
 
class PostEliminar(SuccessMessageMixin, DeleteView): 
    model = Post 
    form = Post
    fields = "__all__"     
 
    
    def get_success_url(self): 
        success_message = 'Post Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('posts')

class PostListView(ListView):
    model = Post
    template_name = 'blog/paginacion.html'
    paginate_by = 2