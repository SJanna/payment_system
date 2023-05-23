from django.db import models

class PaymentMethod(models.Model):
    method_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    # Other fields and relationships as needed