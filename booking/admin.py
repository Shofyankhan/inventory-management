from django.contrib import admin

from .models import (
    Customer,
    Booking,
    Order
)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']

class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Order)

