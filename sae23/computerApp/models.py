from http.client import LENGTH_REQUIRED
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.


class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('MAc - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')) ,
        ('Switch', ('Switch - To maintains and connect servers ')),
    )
    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=6)
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=32, choices=TYPE, default='PC') 

class Personnel(models.Model):
    secu = models.BigIntegerField(
                primary_key= True,
                )

    nom= models.CharField(
                max_length=15)
    
    prenom= models.CharField(
                max_length=15)
                
    
   


