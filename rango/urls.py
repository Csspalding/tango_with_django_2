from django.urls import path
from rango import views
#created 01/08/19 by Cass
#this file handles urls that startwith rango/  

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'), #this url points to the index view function
]
