
from django.contrib import admin
from django.urls import path,include
from users.views import SignUpAPIView, SignInAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # path('api/',include('task1.urls')),
    path('api/signup/', SignUpAPIView.as_view()),
    path('api/signin/', SignInAPIView.as_view())
]
