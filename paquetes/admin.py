from django.contrib import admin
from . models import Departamento,Address,Location,User,Type,Date, State, Package, ShippingOrder
# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ("id_type","type",)
    search_fields = ("id_type",)
    list_filter= ("type",)
    
    
admin.site.register(Departamento)
admin.site.register(Address)
admin.site.register(Location)
admin.site.register(User)
admin.site.register(Type, TypeAdmin)
admin.site.register(Date)
admin.site.register(State)
admin.site.register(Package)
admin.site.register(ShippingOrder)