from django.contrib import admin

# Register your models here.
from products.models import Product,ProductImage,Category,CategoryBanner

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(CategoryBanner)