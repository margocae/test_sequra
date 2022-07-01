from django.db import models

# Create your models here.

class Shopper (models.Model):
	Name = models.TextField()
	email =models.EmailField()
	NIF = models.TextField()