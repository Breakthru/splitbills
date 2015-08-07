from django.db import models

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length=500)
  def __unicode__(self):
    return "%s" % (self.name,)
  
class Recipe(models.Model):
  name = models.CharField(max_length=500)
  ingredients = models.ManyToManyField("Ingredient")
  def __unicode__(self):
    return "%s" % (self.name,)
    