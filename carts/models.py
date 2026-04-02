from django.db import models
from django.contrib.auth import get_user_model
import uuid
from products.models import Product

User = get_user_model()


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Cart'


class CartItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)  # avoid negative quantity

    def __str__(self):
        return f'{self.product.name} x {self.quantity} ({self.cart.user.first_name})'
    

    class Meta:
            unique_together = [['cart', 'product']]
            ordering = ['cart', 'product']
    