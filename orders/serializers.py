from rest_framework import serializers
from orders.models import Order,OrderItem
from carts.serializers import SimpleProductSerializer
from carts.models import Cart

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, value):
        try:
            cart = Cart.objects.get(pk=value)
        except Cart.DoesNotExist:
            raise serializers.ValidationError("No cart found with this id")

        if not cart.items.exists():
            raise serializers.ValidationError("Cart is empty")

        return value

    def create(self,validated_data):
        user_id =  self.context['user_id']
        cart_id = validated_data['cart_id']

        cart = Cart.objects.get(pk=cart_id)
        cart_items = cart.items.select_related('product').all()

        total_price = sum([item.product.price * item.quantity for item in cart_items])

        order = Order.objects.create(user_id=user_id,total_price=total_price)

        order_items = [
            OrderItem(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity,
                total_price=item.product.price * item.quantity
            )
            for item in cart_items
        ]

        OrderItem.objects.bulk_create(order_items)
        cart.delete()

        return order

    def to_representation(self, instance):
        return OrderSerializer(instance).data 

class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    
    class Meta:
        model = OrderItem
        fields = ['id','product','quantity','price','total_price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id','user','status','created_at','updated_at','items']
        read_only_fields = ['user','created_at','updated_at']


