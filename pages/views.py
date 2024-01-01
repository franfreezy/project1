from django.shortcuts import render
#from django.http import HttpResponse //we are not using http again since are using templates

# Create your views here.
def homepage(request):
    return render(request, "blog/blog.html")
