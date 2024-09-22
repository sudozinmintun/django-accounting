from rest_framework.routers import DefaultRouter
from .views import AccountTypesViewSet

router = DefaultRouter()
router.register(r'account-types', AccountTypesViewSet)

urlpatterns = router.urls