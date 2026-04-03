from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from orders.serializers import OrderSerializer,CreateOrderSerializer
from orders.models import Order
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class OrderViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method=='POST':
            return CreateOrderSerializer
        return OrderSerializer
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.prefetch_related('items__product').all()
        return Order.objects.prefetch_related('items__product').filter(user=self.request.user)
