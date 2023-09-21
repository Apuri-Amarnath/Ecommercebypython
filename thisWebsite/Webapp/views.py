from django.shortcuts import render

# Create your views here.
def index(request):
    contextvars={

    }
    return render(request,"index.html", contextvars)
def about(request):
    contextvars={}
    return render(request,"about.html",contextvars)
def product(request):
    contextvars={}
    return render(request,'products.html',contextvars)
def services(request):
    contextvars={}
    return render(request,'services.html',contextvars)
