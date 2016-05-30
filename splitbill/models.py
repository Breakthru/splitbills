from django.db import models

class Card(models.Model):
  """ a credit card """
  name = models.CharField(max_length=16)

class Tag(models.Model):
  """ tag transactions """
  name = models.CharField(max_length=25)
 
class Transaction(models.Model):
  date = models.DateField()
  transaction_date = models.DateField(blank=True)  
  amount = models.IntegerField()
  description = models.TextField()
  tags = models.ManyToManyField(Tag, blank=True)
 
