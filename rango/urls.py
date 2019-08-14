from django.urls import path
from rango import views
#created 01/08/19 by Cass
#this file handles urls that startwith rango/  

app_name = 'rango'
#note the about/ NOT about  - this syntax is very important was the issue with the test not working
urlpatterns = [
    path('', views.index, name='index'), #this url points to the index view function
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
]
