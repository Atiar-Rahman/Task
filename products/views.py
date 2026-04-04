from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from products.models import Category,CategoryBanner,Product,ProductImage,Review
from products.serializers import CategoryBannerSerializer,CategorySerializer,ProductImageSerializer,ProductSerializer,ReviewSerializer
from rest_framework.permissions import IsAuthenticated


class CategoryViewSet(viewsets.ViewSet):
    """
     category model all crud operation
    
    """

    def list(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        category = get_object_or_404(Category,id=pk)
        serializer = CategorySerializer(category)

        return Response(serializer.data)
    
    def create(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        category = get_object_or_404(Category,id=pk)
        serializer = CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk=None):
        category = get_object_or_404(Category,id=pk)
        serializer = CategorySerializer(category,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request,pk=None):
        category = get_object_or_404(Category,id=pk)
        category.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product,id=pk)
        serializer = ProductSerializer(product)

        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        product = get_object_or_404(Product,id=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk=None):
        product = get_object_or_404(Product,id=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        product = get_object_or_404(Product,id=pk)
        product.delete()

        return Response({'message':'delete successfully'},status=status.HTTP_404_NOT_FOUND)
    

class ProductImageViewSet(viewsets.ViewSet):
    def list(self,request):
        images = ProductImage.objects.all()
        serializer = ProductImageSerializer(images,many=True)

        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        image = get_object_or_404(ProductImage, id=pk)
        serializer = ProductImageSerializer(image)
        
        return Response(serializer.data)
    
    def create(self,request):
        serializer = ProductImageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        image = get_object_or_404(ProductImage,id=pk)
        serializer = ProductSerializer(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk=None):
        image = get_object_or_404(ProductImage,id=pk)
        serializer = ProductSerializer(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        image = get_object_or_404(ProductImage, id=pk)
        image.delete()

        return Response({'message':"product image delete successfully"}, status=status.HTTP_204_NO_CONTENT)


class CategoryBannerViewSet(viewsets.ViewSet):
    def list(self,request):
        banners = CategoryBanner.objects.all()
        serializer = CategoryBannerSerializer(banners,many=True)

        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        banner = get_object_or_404(CategoryBanner, id=pk)
        serializer = CategoryBannerSerializer(banner)
        
        return Response(serializer.data)
    
    def create(self,request):
        serializer = CategoryBannerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        image = get_object_or_404(CategoryBanner,id=pk)
        serializer = CategoryBannerSerializer(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk=None):
        image = get_object_or_404(CategoryBanner,id=pk)
        serializer = CategoryBannerSerializer(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        image = get_object_or_404(CategoryBanner, id=pk)
        image.delete()

        return Response({'message':"Category banner delete successfully"}, status=status.HTTP_204_NO_CONTENT)


# CategoryProduct viewset

class CategoryProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Product.objects.none()  # Swagger generation safe
        category_id = self.kwargs.get('category_pk')
        return Product.objects.filter(category_id=category_id)
    
    def perform_create(self, serializer):
        serializer.save(category_id=self.kwargs.get('category_pk'))




class ProductReviewViewset(viewsets.ModelViewSet):
    
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        reviews= Review.objects.filter(product_id=self.kwargs.get('product_pk'))

        return reviews
    

    def get_serializer_context(self):
        return {'product_id': self.kwargs.get('product_pk'),'user': self.request.user}
    

