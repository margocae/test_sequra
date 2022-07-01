from django.db import models

# Create your models here.

class Order (models.Model):
	
	merchant = models.ForeignKey(model.Merchant, on_delete=models.CASCADE)
	shopper = models.ForeignKey(model.Shopper, on_delete=models.CASCADE)
	Amount = models.DecimalField(max_digit=20,decimal_places=2)
	Created =models.DateTimeField()
	Completed = models.DateTimeField()