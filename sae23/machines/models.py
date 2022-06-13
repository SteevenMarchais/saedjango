from black import prev_siblings_are
from django.db import models
from datetime import datetime

from personnels.models import Personnel


# Create your models here.

class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('MAc - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')) ,
        ('Switch', ('Switch - To maintains and connect servers ')),
    )
    id = models.AutoField(primary_key=True, editable=False)
    proprietaire = models.BigIntegerField()
    proprietaire = models.ForeignKey(Personnel, null=True, on_delete=models.SET_NULL)
    infra = models.CharField(max_length=200)
    maintenanceDate = models.DateField(default = datetime.now())


     