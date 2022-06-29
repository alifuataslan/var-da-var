from multiprocessing import context
from django.shortcuts import render

from accounts.models import Yemekler

# Create your views here.
def index(request):
    yemekler=Yemekler.objects.all()
    context={
        "yemekler":yemekler
    }
    return render(request,"index-6.html",context)

