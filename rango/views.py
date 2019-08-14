from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import reverse

from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm
from rango.forms import UserForm
from rango.forms import UserProfileForm
# Create your views here.
#index view is the home page for the project
#view handles responce to request from client

#notice capital letter for name in HTML is not the same as variable name in urls.py
def index(request):
  #To test return HttpResponse("Rango says hey there partner! <a href='/rango/about'>About</a>")

  #query db for a list of ALL categories stored, ordered by likes in -decending order limit display to 5
  category_list = Category.objects.order_by('-likes')[:5]
  page_list = Page.objects.order_by('views')[:5]
  
  #construct a dictionary to pass to the template engine as its context.
  context_dict = {}#initialise dictionary
  context_dict['boldmessage']='Crunchy, creamy, cookie, candy, cupcake!'
  context_dict ['categories' ]=category_list
  context_dict ['pages' ]=page_list
  #return a rendered responce to send to the client
  #make use of shortcut function 
  return render(request, 'rango/index.html', context=context_dict)
 
def about(request):
  #print out if GET or POST request
  print (request.method)
  #prints out username if none logged in prints'anonymousUser'
  print(request.user)
  context ={'boldmessage': 'This tutorial has been put together by Cassie'}
  return render(request, 'rango/about.html', context)#third parameter not needed as empty context dictionary
#now mapp your Url to the view

def show_category(request, category_name_slug):#stores encoded category name
  context_dict = {} #initialise dictionary
  #extract data from the model, add it to context_dic, handle exception render reponce. 
  try:
    # get () returns DoesNotExist // try/catch  handles exception if no categories exist
    # or returns a model instance
    category= Category.objects.get(slug=category_name_slug)

    #filter()  will return a list of page objects or an empty list
    pages= Page.objects.filter(category=category)

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

#this method saves user data into a form
def add_category(request):
    form = CategoryForm()

    if request.method =='POST':
      form = CategoryForm(request.POST)

    #if a valid new form is returned above
    if form.is_valid():
      #Save the new form to the db, reference cat is the instance of the category object created by the form
      cat = form.save(commit=True)
      print(cat,cat.slug)#prints the category to the console 
      #place a confirmation messge next if nec //not this time
      #instead in this case the most recent category added is on the index page we redirect to index page
      return index(request)
    else:
      #error in form so print them to terminal //todo in html template handle the bad form or no form case
      return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
  try:
    category = Category.objects.get(slug=category_name_slug)
  except Category.DoesNotExist:
    category = None

  form = PageForm()
  if request.method =='POST':
    form = PageForm(request.POST)

    if form.is_valid():
      if category:
        page = form.save(commit=False)
        page.category = category
        page.view =0
        page.save()
    #once page form is created redirect user to the show_category() view
    #if a match is found from show_category ()the complete url is returned
    #as an added complication show_category(category_name_slug) passed in parameter
    #by providing a value in dictionary as kwargs to the reverse() it can formulate the url
        return redirect(reverse('rango:show_category',kwargs={'category_name_slug':category_name_slug}))
    else:
      print (form.errors)
  context_dict = {'form':form, 'category':category} #objects passed through the template context dictionary to the html
  return render(request, 'rango/add_page.html',context=context_dict)

def register(request):
  registered = False
  if request.method == 'POST':
    user_form = UserForm(data=request.POST)
    profile_form = UserProfileForm(data=request.POST)
    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()
      profile = profile_form.save(commit=False)
      profile.user = user
      if 'picture' in request.FILES:
        profile.picture = request.FILES['picture']
      profile.save()
      registered = True
    else:
      print(user_form.errors, profile_form.errors) 
  else: 
    user_form = UserForm()
    profile_form = UserProfileForm() 
  return render (request,'rango/register.html', {'user_form': user_form,'profile_form': profile_form,'registered': registered})


