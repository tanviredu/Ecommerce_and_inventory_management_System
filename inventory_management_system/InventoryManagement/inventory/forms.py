from django import forms
from .models import Laptop,Desktop,Mobile

class LaptopForm(forms.ModelForm):
    class Meta:
        model  = Laptop
        fields = ('type_of_device','price','status','issue')

class DesktopForm(forms.ModelForm):
    class Meta:
        model  = Desktop
        fields = ('type_of_device','price','status','issue')



class MobileForm(forms.ModelForm):
    class Meta:
        model  = Mobile
        fields = ('type_of_device','price','status','issue')
        


        