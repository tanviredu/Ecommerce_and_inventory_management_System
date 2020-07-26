from django.shortcuts import render
from .models import Laptop,Desktop,Mobile
from .forms import LaptopForm,DesktopForm,MobileForm


def index(request):
    return render(request,'inventory/index.html')


def display_laptops(request):
    ## get all the laptops
    items = Laptop.objects.all()
    context = {
        'items' : items,
        'header': "Laptop" 
    }
    return render(request,'inventory/index.html',context)