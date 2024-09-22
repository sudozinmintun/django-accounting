from rest_framework import viewsets
from .models import AccountClassification
from .serializers import AccountClassificationSerializer

class AccountClassificationViewSet(viewsets.ModelViewSet):
    queryset = AccountClassification.objects.all()
    serializer_class = AccountClassificationSerializer
