from django.contrib import admin

from .models import Users, Packages,Invoices,UserAndinvoice
# Register your models here.

admin.site.register(Users)
admin.site.register(Packages)
admin.site.register(Invoices)
admin.site.register(UserAndinvoice)
