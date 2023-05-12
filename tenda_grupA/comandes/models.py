from django.db import models
from carreto.models import Carreto
# Comanda es com historial de tots els carretons estiguin 'comprat' o 'no'
class Comanda(models.Model):
    #Entenc que un usuari te diferents comandes 
    idComanda = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    #Cada comanda te diferent carretoms
    carretons = models.ManyToManyField(Carreto)
    #que poden estar finalizades(comprades)
    esComprat = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} - {}".format(self.idComanda, self.esComprat)
