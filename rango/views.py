from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#index view is the home page for the project
#view handles responce to request from client

#notice capital letter for name in HTML is not the same as variable name in urls.py
def index(request):
  return HttpResponse("Rango says hey there partner <a href='/rango/about'>About</a>")
  # this worked click and paste link "http://127.0.0.1:8000/rango/about"

def about(request):
  return HttpResponse("Rango says here is the About Page <a href='/rango/'>Index</a>")

#now mapp your Url to the view