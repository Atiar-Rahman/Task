from django.contrib import admin

# Register your models here.
from carts.models import CartItem,Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user']


admin.site.register(CartItem)