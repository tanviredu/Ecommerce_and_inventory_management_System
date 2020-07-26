from django.shortcuts import render
from .models import Laptop,Desktop,Mobile
from .forms import LaptopForm,DesktopForm,MobileForm


def index(request):
    return render(request,'inventory/index.html')
    
