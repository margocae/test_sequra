from django.db import models

# Create your models here.
class Merchant (models.Model):
	Name = models.TextField()
	email =models.EmailField()
	CIF = models.TextField()