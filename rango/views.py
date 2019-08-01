from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#index view is the home page for the project
#view handles responce to request from client

def index(request):
  return HttpResponse("Rango says hey there partner")

#now mapp your Url to the view