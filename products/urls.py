from django.urls import path,include
from products.views import CategoryViewSet,ProductViewSet,ProductImageViewSet,CategoryBannerViewSet,CategoryProductViewset,ProductReviewViewset
from carts.views import CartViewSet, CartItemViewSet
from orders.views import OrderViewset
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register('categorys',CategoryViewSet,basename='category'),
router.register('products',ProductViewSet,basename='products'),
router.register('product-image',ProductImageViewSet,basename='product-image'),
router.register('category-banner',CategoryBannerViewSet,basename='category-banner'),
router.register('carts',CartViewSet,basename='carts'),
router.register('orders',OrderViewset,basename='orders')

category_router = routers.NestedDefaultRouter(router, 'categorys', lookup='category')
category_router.register('products',CategoryProductViewset,basename='category-product')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews',ProductReviewViewset,basename='product_review')
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')
urlpatterns = [
    path('',include(router.urls)),
    path('',include(category_router.urls)),
    path('',include(product_router.urls)),
    path('',include(cart_router.urls)),
]
