from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(product)
admin.site.register(order)
admin.site.register(placeOrder)
admin.site.register(orderStatus)
admin.site.register(review)