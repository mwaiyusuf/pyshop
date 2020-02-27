from django.shortcuts import render
# from the django.http module we are importing the HttpResponse class
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    products = Product.objects.all()
 # we are creating an instance of this class HttpResponse
    return HttpResponse('welcome to the first trial')
# def new(request):
#     return HttpResponse("arrival of new products")