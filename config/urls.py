
from django.contrib import admin
from django.urls import path,include
from users.views import SignUpAPIView, SignInAPIView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # path('api/',include('task1.urls')),
    path('api/signup/', SignUpAPIView.as_view()),
    path('api/signin/', SignInAPIView.as_view()),
    path('api/',include('products.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)