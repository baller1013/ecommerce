from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem


#register the mnodel on the admin

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
