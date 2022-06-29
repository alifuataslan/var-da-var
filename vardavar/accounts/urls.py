from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from foot import views
app_name ="foot"

urlpatterns = [
    path('',views.index,name="index"),
   

]