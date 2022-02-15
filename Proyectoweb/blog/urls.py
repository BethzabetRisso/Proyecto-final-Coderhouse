from django.urls import path
from . import views
from blog.views import PostDetalle, PostCrear, PostActualizar, PostEliminar
urlpatterns = [
    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),

    # path('posts/', PostListado.as_view(template_name = "blog/index.html"), name='posts'),
 
    path('post/detalle/<int:pk>', PostDetalle.as_view(template_name = "blog/detalles.html"), name='detalles'),
 
    path('post/crear', PostCrear.as_view(template_name = "blog/crear.html"), name='crear'),
 
    path('post/editar/<int:pk>', PostActualizar.as_view(template_name = "blog/actualizar.html"), name='actualizar'), 
 
    path('post/eliminar/<int:pk>', PostEliminar.as_view(), name='eliminar'),    
]
