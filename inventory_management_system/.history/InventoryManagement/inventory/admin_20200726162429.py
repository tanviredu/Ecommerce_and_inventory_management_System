from django.contrib import admin
from .models import Mobile,Desktop,Laptop

admin.models.register(Mobile)
admin.models.register(Desktop)
admin.models.register(Laptop)


# Register your models here.
