from django.db import models

class AccountClassification(models.Model):
    account_name = models.CharField(max_length=100)
    account_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.account_name