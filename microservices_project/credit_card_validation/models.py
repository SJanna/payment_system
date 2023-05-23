# models.py
from django.db import models

class CreditCard(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    card_type = models.CharField(max_length=20)

    # Other fields and relationships as needed