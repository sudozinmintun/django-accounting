from rest_framework import serializers
from .models import AccountTypes
from account_classification.serializers import AccountClassificationSerializer  # Adjust import path


class AccountTypesSerializer(serializers.ModelSerializer):
    account_classification = AccountClassificationSerializer()

    class Meta:
        model = AccountTypes
        fields = ['id', 'account_name', 'account_code', 'description', 'financial_statement', 'account_classification']