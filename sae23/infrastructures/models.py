from django.db import models
from datetime import datetime
# Create your models here.

class Infrastructures(models.Model):

    nom = models.CharField(
                max_length=15,
                primary_key = True)
    
    position = models.CharField(
                max_length=15)

    machine = models.SmallIntegerField(
                )

    personnel = models.CharField(
                max_length=15)
                
    
    responsable = models.CharField(
                max_length=15)

    date_de_maintenance = models.DateField(
                default = datetime.now())