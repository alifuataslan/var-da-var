from django.urls import path

from . import views
app_name ="foot"

urlpatterns = [
    path('',views.index,name="index"),
   

]