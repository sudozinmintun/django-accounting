from rest_framework import serializers
from .models import AccountClassification


class AccountClassificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountClassification
        fields = ['id', 'account_name', 'account_code']