from django.db import models
from datetime import datetime


# Create your models here.

class Personnel(models.Model):
    secu = models.BigIntegerField(
                primary_key= True,
                )

    nom = models.CharField(
                max_length=15)
    
    prenom = models.CharField(
                max_length=15)

    machine_perso = models.SmallIntegerField(
                )

    lieu_travail = models.CharField(
                max_length=15)

    date_de_maintenance = models.DateField(default = datetime.now())

