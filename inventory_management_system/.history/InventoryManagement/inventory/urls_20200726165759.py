from django.urls import path, include
from . import views

app_name = 'inventory'

urlpatterns = [
    path("",views.index,name='index'),
    path("laptop/",views.display_laptops,name="laptops"),
    path("desktop/",views.display_laptops,name="desktops"),
    path("mobile/",views.display_laptops,name="mobiles"),
    
]