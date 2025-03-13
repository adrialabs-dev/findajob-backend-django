from rest_framework.routers import DefaultRouter

from .viewsets import JobViewSet

router = DefaultRouter()
router.register('jobs', JobViewSet)

urlpatterns = router.urls