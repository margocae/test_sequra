from django.db import models

# Create your models here.

class Merchant (models.Model):
	Name = models.TextField()
	email =models.EmailField()
	CIF = models.TextField()

class Shopper (models.Model):
	Name = models.TextField()
	email =models.EmailField()
	NIF = models.TextField()

class Order (models.Model):
	merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
	shopper = models.ForeignKey(Shopper, on_delete=models.CASCADE)
	Amount = models.DecimalField(max_digits=20,decimal_places=2)
	Created =models.DateTimeField(blank=True)
	Completed = models.DateTimeField(null=True,blank=True)

class Disbursements (models.Model):
	merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
	week = models.DecimalField(max_digits=2,decimal_places=0)
	disbursement = models.DecimalField(max_digits=20,decimal_places=2)