from rest_framework.routers import DefaultRouter
from .views import AccountClassificationViewSet

router = DefaultRouter()
router.register(r'account-classifications', AccountClassificationViewSet)

urlpatterns = router.urls
