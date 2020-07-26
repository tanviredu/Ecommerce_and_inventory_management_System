from django.urls import path, include
from . import views

app_name = 'inv'

urlpatterns = [
    path("",views.index,name='index'),
    path("laptop/",views.display_laptops,name="laptops"),
    path("desktop/",views.display_desktops,name="desktops"),
    path("mobile/",views.display_mobiles,name="mobiles"),
    path("create_mobile/",views.CreateMobileView.as_view(),name="c_mobile"),
    path("edit_mobile/",views.EditMobileView.as_view(),name="e_mobile"),
    
    path("create_desktop/",views.CreateDesktopView.as_view(),name="c_desktop"),
    path("create_laptop/",views.CreateLaptopView.as_view(),name="c_laptop"),
    
]