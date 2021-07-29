from django.db import models
from django.utils import timezone

class Product(models.Model):
	name = models.CharField(max_length=100)
	cost = models.IntegerField()
	price = models.IntegerField()
	def profit(self):
		return self.price - self.cost

class Transaction(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	recieved = models.BooleanField(default=False)
	paid = models.BooleanField(default=False)
	who = models.CharField(max_length=100)
	date = models.DateTimeField(editable=False, default=timezone.now)
