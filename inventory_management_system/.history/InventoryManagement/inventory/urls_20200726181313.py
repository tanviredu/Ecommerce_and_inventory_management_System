from django.urls import path, include
from . import views

app_name = 'inv'

urlpatterns = [
    path("",views.index,name='index'),
    path("laptop/",views.display_laptops,name="laptops"),
    path("desktop/",views.display_desktops,name="desktops"),
    path("mobile/",views.display_mobiles,name="mobiles"),
    path("create_mobile/",views.CreateMobileView.as_view(),name="c_mobile"),
    path("edit_mobile/<int:pk>",views.EditMobileView.as_view(),name="e_mobile"),
    path("create_desktop/",views.CreateDesktopView.as_view(),name="c_desktop"),
    path("edit_desktop/<int:pk>",views.EditDesktopView.as_view(),name="e_desktop"),
    path("create_laptop/",views.CreateLaptopView.as_view(),name="c_laptop"),
    path("edit_laptop/<int:pk>",views.EditlaptopView.as_view(),name="e_laptop"),
    path("delete_laptop/<int:pk>",views.DeletelaptopView.as_view(),name="d_laptop"),
    path("delete_desktop/<int:pk>",views.DeleteDesktopsView.as_view(),name="d_desktop"),
    path("delete_mobile/<int:pk>",views.DeleteMobileView.as_view(),name="d_mobile"),
    
]