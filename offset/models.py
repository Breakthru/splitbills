from django.db import models

# Create your models here.
class Transaction(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    type = models.CharField(max_length=200)
    date = models.DateField('transaction date')
    def __unicode__(self):
        return str(self.date)+": "+self.type+" "+str(self.amount)
    class Meta:
        ordering = ["date"]

class Mortgage(models.Model):
    credit_limit = models.DecimalField(decimal_places=2, max_digits=8)
    initial_balance = models.DecimalField(decimal_places=2, max_digits=8)
    start_date = models.DateField('start date')
    initial_rate = models.DecimalField(decimal_places=2,max_digits=6)
    term = models.IntegerField('duration in months')
    
