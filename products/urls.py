# we are importing the path function
from django.urls import path
# we av to import the viewa module
from . import  views
# , means the current folder
# and the module ends up to be an object
urlpatterns =[
    path('', views.index)
]