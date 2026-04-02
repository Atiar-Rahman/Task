from rest_framework.routers import SimpleRouter
from products.views import CategoryViewSet,ProductViewSet,ProductImageViewSet,CategoryBannerViewSet


router = SimpleRouter()

router.register('categorys',CategoryViewSet,basename='category'),
router.register('products',ProductViewSet,basename='products'),
router.register('product-image',ProductImageViewSet,basename='product-image'),
router.register('category-banner',CategoryBannerViewSet,basename='category-banner'),



urlpatterns = router.urls
