from django.shortcuts import render
from .models import Laptop,Desktop,Mobile
from .forms import LaptopForm,DesktopForm,MobileForm
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

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


class EditMobileView(UpdateView):
    form_class = MobileForm
    template_name = "inventory/edit_form.html"
    model = Mobile
    
class DeleteMobileView(DeleteView):
    model = Mobile
    success_url = reverse_lazy('inv:mobiles')


class CreateLaptopView(CreateView):
    form_class = LaptopForm
    template_name = "inventory/create_item.html"

class EditlaptopView(UpdateView):
    form_class = LaptopForm
    template_name = "inventory/edit_form.html"
    model = Laptop
    
class DeletelaptopView(DeleteView):
    model = Laptop
    success_url = reverse_lazy('inv:laptops')


class CreateDesktopView(CreateView):
    form_class = DesktopForm
    template_name = "inventory/create_item.html"


class EditDesktopView(UpdateView):
    form_class = DesktopForm
    template_name = "inventory/edit_form.html"
    model = Desktop

class DeleteDesktopsView(DeleteView):
    model = Desktop
    success_url = reverse_lazy('inv:desktops')
