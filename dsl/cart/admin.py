from django.contrib import admin
from .models import NewOrder, OrderProduct

admin.site.register(NewOrder)
admin.site.register(OrderProduct)

