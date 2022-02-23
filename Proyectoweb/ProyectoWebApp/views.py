from django.shortcuts import render, HttpResponse
# aca se importa el model de la app servicios


# Create your views here.
def home(request):
    return render(request, 'ProyectoWebApp/home.html')

def AcercaDeMi(request):
    print("estoy aca")
    return render(request, 'ProyectoWebApp/acercademi.html')
