from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account_classification.views import AccountClassificationViewSet
from account_types.views import AccountTypesViewSet


router = DefaultRouter()
router.register(r'account-classifications', AccountClassificationViewSet)
router.register(r'account-types', AccountTypesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
]
