from django.db import models

class TransactionLog(models.Model):
    transaction_id = models.IntegerField()
    success = models.BooleanField(default=False)

    # Other fields and relationships as needed
