from django.db import models

class Tag(models.Model):
  """ tag transactions """
  name = models.CharField(max_length=25)
 
class Transaction(models.Model):
  date = models.DateField()
  amount = models.IntegerField()
  description = models.TextField()
  tags = models.ManyToManyField(Tag, blank=True)
 
