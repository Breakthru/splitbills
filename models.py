from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User)

class Transaction(models.Model):
    account = models.ForeignKey(Account)
    date = models.DateField()
    amount = models.IntegerField()
    description = models.TextField()
