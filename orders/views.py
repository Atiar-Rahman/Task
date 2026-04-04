from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from orders.serializers import OrderSerializer,CreateOrderSerializer,OrderUpdateSerializer,EmptySerializer
from orders.models import Order
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import action
from orders.services import OrderService

# Create your views here.


class OrderViewset(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options', 'trace']
  
    @action(detail=True, methods=['get','post'], permission_classes=[IsAuthenticated])
    def cancel(self,request, pk=None):
        order = self.get_object()
        OrderService.cancel_order(order=order,user=request.user)
        return Response({'status':'Order canceled'})

    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    def update_status(self,request,pk=None):
        order = self.get_object()
        serializer = OrderUpdateSerializer(order,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': f'Order status updated to {request.data['status']}'})
    def get_permissions(self):
        if self.request.method in ['PATCH','DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]


    def get_serializer_class(self):
        if self.action=='cancel':
            return EmptySerializer
        elif self.request.method=='POST':
            return CreateOrderSerializer
        elif self.request.method=='PATCH':
            return OrderUpdateSerializer
        return OrderSerializer
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.prefetch_related('items__product').all()
        return Order.objects.prefetch_related('items__product').filter(user=self.request.user)
