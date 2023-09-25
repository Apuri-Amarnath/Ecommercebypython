from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    contextvars={

    }
    return render(request,"index.html", contextvars)
def about(request):
    contextvars={}
    return render(request,"about.html",contextvars)
def products(request):
    products = Product.objects.all()
    contextvars={'products':products}
    return render(request,'products.html',contextvars)
def services(request):
    contextvars={}
    return render(request,'services.html',contextvars)
