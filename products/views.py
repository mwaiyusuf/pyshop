# from django.shortcuts import render
# from the django.http module we are importing the HttpResponse class
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .email import send_welcome_email


# Create your views here.

def index(request):
    if request.method =='POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your _name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponse(index )
        else:
            form = NewsLetterForm()
        return render(request, '')
    products = Product.objects.all()
    # products = Product.objects.get/save()
# renders the request of data to be passed using the dictionary
    return render(request, 'index.html', {'products':products})
 # we are creating an instance of this class HttpResponse
 #    return HttpResponse('welcome to the first trial')
# def new(request):
#     return HttpResponse("arrival of new products")