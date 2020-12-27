from django.contrib import admin

from .models import DataRegister, LoginPassword, RegisterObject

admin.site.register(DataRegister)
admin.site.register(LoginPassword)
admin.site.register(RegisterObject)
