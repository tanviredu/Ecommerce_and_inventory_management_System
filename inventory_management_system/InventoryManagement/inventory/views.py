from django.shortcuts import render
from .models import Laptop,Desktop,Mobile
from .forms import LaptopForm,DesktopForm,MobileForm
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView,ListView,UpdateView,DetailView

def index(request):
    #return render(request,'inventory/index.html')
    return redirect('inv:laptops')


def display_laptops(request):
    ## get all the laptops
    items = Laptop.objects.all()### all the edit and the create and delete will be function based

    context = {
        'items' : items,
        'header': "Laptop" 
    }
    return render(request,'inventory/index.html',context)



def display_desktops(request):
    ## get all the laptops
    items = Desktop.objects.all()
    context = {
        'items' : items,
        'header': "Desktop" 
    }
    return render(request,'inventory/index.html',context)


def display_mobiles(request):
    ## get all the laptops
    items = Mobile.objects.all()
    context = {
        'items' : items,
        'header': "mobile" 
    }
    return render(request,'inventory/index.html',context)




class CreateMobileView(CreateView):
    form_class = MobileForm
    template_name = "inventory/create_item.html"


class CreateLaptopView(CreateView):
    form_class = LaptopForm
    template_name = "inventory/create_item.html"


class CreateDesktopView(CreateView):
    form_class = DesktopForm
    template_name = "inventory/create_item.html"
