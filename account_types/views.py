from rest_framework import viewsets
from .models import AccountTypes
from .serializers import AccountTypesSerializer

class AccountTypesViewSet(viewsets.ModelViewSet):
    queryset = AccountTypes.objects.all().select_related('account_classification')
    serializer_class = AccountTypesSerializer
