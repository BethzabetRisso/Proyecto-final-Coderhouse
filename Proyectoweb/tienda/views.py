from django.shortcuts import render
from .models import Producto
from django.views.generic.list import ListView

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    return render(request,'tienda/tienda.html',{"productos":productos})


# def categoria(request, categoria_id):

#     categoria = Categoria.objects.get(id=categoria_id)
#     posts = Post.objects.filter(categorias =categoria)

#     return render(request, "blog/categoria.html", {"categoria": categoria,"posts": posts})


#paginacion
class ProductoListView(ListView):
    model = Producto
    template_name = 'tienda/paginacion.html'
    paginate_by = 2