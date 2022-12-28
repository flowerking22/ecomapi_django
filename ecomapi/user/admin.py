from django.contrib import admin
from .models import usermodel,useraddressmodel
# Register your models here.
admin.site.register(usermodel)
admin.site.register(useraddressmodel)