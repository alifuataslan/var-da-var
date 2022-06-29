from multiprocessing import context
from unicodedata import category
from django.shortcuts import render

from .models import Catagori

# Create your views here.
# Create your views here.
def index(request):
    category_foot= Catagori.objects.all()
    context={
        "category_foot":category_foot
    }
  
    return render(request,"index-6.html",context)

def login(request):
    return render(request,"loginandregister.html")