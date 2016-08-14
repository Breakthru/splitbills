from django.db import models

class Account(models.Model):
    name = models.TextField()
    type = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)


class Tag(models.Model):
  """ tag transactions """
  name = models.CharField(max_length=25)
  def __str__(self):
      return str(self.name)


class Transaction(models.Model):
  account = models.ForeignKey(Account)
  date = models.DateField()
  amount = models.IntegerField()
  description = models.TextField()
  tags = models.ManyToManyField(Tag, blank=True)
  def __str__(self):
    return str(self.date)+" "+str(self.amount)
