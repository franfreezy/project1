from django.shortcuts import render
#from django.http import HttpResponse //we are not using http again since are using templates

# Create your views here.
def homepage(request):
    return render(request, "home/home.html")

def portfolio(request):
    return render(request, "home/portfolio.html")

def homeauto(request):
    return render(request, "home/homeauto.html")

def blog(request):
    return render(request, "home/blog.html")

def docs(request):
    return render(request, "home/docs.html")