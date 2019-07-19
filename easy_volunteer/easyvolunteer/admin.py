from django.contrib import admin
from .models import CUser, Organ, Service, Area, Job, Product, Brand

admin.site.register(CUser)
admin.site.register(Organ)
admin.site.register(Service)
admin.site.register(Area)
admin.site.register(Job)
admin.site.register(Product)
admin.site.register(Brand)

# Register your models here.
