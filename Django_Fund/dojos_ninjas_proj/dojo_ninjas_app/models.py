from django.db import models
from django.db.models.deletion import CASCADE

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    desc = models.TextField(default="Enter a description... ")

class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos, related_name="ninjas", on_delete= models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)