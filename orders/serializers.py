from rest_framework import serializers
from orders.models import Order,OrderItem
from carts.serializers import SimpleProductSerializer
from carts.models import Cart
from orders.services import OrderService

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

        try:
            order = OrderService.order_create(user_id=user_id,cart_id=cart_id)
            return order
        except ValueError as e:
            raise serializers.ValidationError(str(e))
        

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


