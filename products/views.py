from django.shortcuts import render
# from the django.http module we are importing the HttpResponse class
from django.http import HttpResponse

# Create your views here.

def index(request):
 # we are creating an instance of this class HttpResponse
    return HttpResponse('welcome to the first trial')
def new(request):
    # return HttpResponse("arrival of new products")