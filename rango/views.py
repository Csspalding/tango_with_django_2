from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category, Page

# Create your views here.
#index view is the home page for the project
#view handles responce to request from client

#notice capital letter for name in HTML is not the same as variable name in urls.py
def index(request):
  #To test return HttpResponse("Rango says hey there partner! <a href='/rango/about'>About</a>")

  #query db for a list of ALL categories stored, ordered by likes in -decending order limit to 5
  category_list = Category.objects.order_by('-likes')[:5]


  #construct a dictionary to pass to the template engin as its context.
  #Note the key boldmessage is the dame as {{boldmessage}} in the template
  context_dict = {}
  context_dict['boldmessage']='Crunchy, creamy, cookie, candy, cupcake!'
  context_dict['categories'] = category_list
  #return a rendered responce to send to the client
  #make use of shortcut function 
  return render(request, 'rango/index.html', context=context_dict)
 
def about(request):
  context_dict={'boldmessage': 'This tutorial has been put together by Cassie'}
  return render(request, 'rango/about.html', context=context_dict)
#now mapp your Url to the view

def show_category(request, category_name_slug):#stores encoded category name
  context_dict = {} #initialise dictionary
  #extract data from the model, add it to context_dic, handle exception render reponce. 
  try:
    # get () returns DoesNotExist // try/catch  handles exception if no categories exist
    # or returns a model instance
    category = Category.objects.get(slug=category_name_slug)

    #filter()  will return a list of page objects or an empty list
    pages = Page.objects.filter(category=category)

    #Saves results from filter() to template context under name pages
    context_dict['pages'] = pages
    #adds the category object from db to the context dictionary
    # which is used to verify it exists in the template 
    context_dict['category']= category
  except Category.DoesNotExist:
    #set context_dict to None as none found, DoesNotExist exception is displayed
    context_dict['pages'] = None 
    context_dict['category']= None 
  #render the request as a responce to the client
  return render(request, 'rango/category.html', context=context_dict)