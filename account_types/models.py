from django.db import models
from account_classification.models import AccountClassification

class AccountTypes(models.Model):
    account_name = models.CharField(max_length=100)
    account_code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=100)
    financial_statement = models.CharField(max_length=100)
    account_classification = models.ForeignKey(AccountClassification, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_name