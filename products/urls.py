# we are importing the path function
from django.urls import path
# we av to import the viewa module
from . import  views
# , mean s the current folder
# and the module ends up to be an object
urlpatterns =[
# the quotes are left empty to show the root of the app in routing
    path('', views.index)
]