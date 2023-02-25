from django.contrib import admin
from . models import *
# Register your models here.
class catAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
admin.site.register(Category,catAdmin)

class proAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
    list_display = ['name','price','stock','available']
    list_editable = ['price','stock','available',]
    list_editable = ['price','stock','available',]
admin.site.register(Products,proAdmin)