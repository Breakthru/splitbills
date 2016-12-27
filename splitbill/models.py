from django.db import models

class Account(models.Model):
    name = models.TextField()
    type = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)


class Statement(models.Model):
    date_added = models.DateTimeField()
    account = models.ForeignKey(Account)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.date_to)


class Tag(models.Model):
  """ tag transactions """
  name = models.CharField(max_length=25)
  def __str__(self):
      return str(self.name)


class RawTransaction(models.Model):
    raw_data = models.TextField()
    date_added = models.DateTimeField()
    account = models.ForeignKey(Account)
    statement = models.ForeignKey(Statement)

    ordering = ['-date_added']
    def __str__(self):
        return self.raw_data


class Transaction(models.Model):
  account = models.ForeignKey(Account)
  statement = models.ForeignKey(Statement)
  raw = models.ForeignKey(RawTransaction)
  date = models.DateField()
  amount = models.IntegerField()
  description = models.TextField()
  tags = models.ManyToManyField(Tag, blank=True)

  ordering = ['-date']

  def __str__(self):
    return str(self.date)+" "+str(self.amount)
  @property
  def display_amount(self):
      return u"\xA3 %1.02f" % (self.amount / 100.0,)

class RawLabels(models.Model):
    """ Raw labels data collected by user """
    transaction = models.ForeignKey(RawTransaction)
    tag = models.ForeignKey(Tag)
