from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#index view is the home page for the project
#view handles responce to request from client

#notice capital letter for name in HTML is not the same as variable name in urls.py
def index(request):
  #return HttpResponse("Rango says hey there partner! <a href='/rango/about'>About</a>")

  #construct a dictionary to pass to the template engin as its context.
  #Note the key boldmessage is the dame as {{boldmessage}} in the template
  context_dict= {'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}
  #return a rendered responce to send to the client
  #make use of shortcut function 
  return render(request, 'rango/index.html', context=context_dict)
 
def about(request):
  context_dict={'boldmessage': 'This tutorial has been put together by Cassie'}

  #return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
  return render(request, 'rango/about.html', context=context_dict)
#now mapp your Url to the view