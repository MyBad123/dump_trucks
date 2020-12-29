from django.contrib import admin

from .models import DataRegister, LoginPassword, RegisterObject, Order, Truck

admin.site.register(DataRegister)
admin.site.register(LoginPassword)
admin.site.register(RegisterObject)
admin.site.register(Order)
admin.site.register(Truck)

