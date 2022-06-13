from django.db import models
from datetime import datetime
from machines.models import Machine
from personnels.models import Personnel
# Create your models here.

class Infrastructures(models.Model):

    nom = models.CharField(max_length=15, primary_key = True)
    position = models.CharField(max_length=200)
    responsable = models.BigIntegerField()
    responsable=models.ForeignKey(Personnel, null=True, on_delete=models.SET_NULL)
    date_de_maintenance = models.DateField(default = datetime.now())

   
    