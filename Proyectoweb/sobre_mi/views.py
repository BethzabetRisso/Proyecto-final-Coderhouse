from django.shortcuts import render

def about(request):
    return render(request,'sobre_mi/about.html')
