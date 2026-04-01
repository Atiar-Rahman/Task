
from rest_framework.routers import DefaultRouter
from task1.views import StudentViewSet,StudentDetailsViewSet

router = DefaultRouter()

router.register('students',StudentViewSet, basename='student')
router.register('student-details',StudentDetailsViewSet, basename='student-details')


urlpatterns = router.urls
