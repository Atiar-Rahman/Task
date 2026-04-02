from rest_framework import serializers
from products.models import Category, CategoryBanner, Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )

    class Meta:
        model = ProductImage
        fields = [
            'id', 'product', 'images', 'alt_text', 'is_featured',
            'created_at', 'updated_at'
        ]



class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)  # nested images
    category_name = serializers.CharField(source='category.name', read_only=True)  # optional

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'category', 'category_name',
            'price', 'discount_price', 'description',
            'stock', 'is_active', 'created_at', 'updated_at', 'images'
        ]


class CategoryBannerSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = CategoryBanner
        fields = [
            'id', 'category', 'images', 'title', 'subtitle',
            'cta_text', 'cta_url', 'is_featured', 'created_at', 'updated_at'
        ]


class CategorySerializer(serializers.ModelSerializer):
    banners = CategoryBannerSerializer(many=True, read_only=True)  # nested banners
    products = ProductSerializer(many=True, read_only=True)  # nested products

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'description', 'created_at', 'updated_at',
            'banners', 'products'
        ]

    