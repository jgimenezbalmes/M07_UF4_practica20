from django.db import models
from carreto.models import Carreto
from login.models import User
# Comanda es com historial de tots els carretons estiguin 'comprat' o 'no'
class Comanda(models.Model):
    #Entenc que un usuari te diferents comandes 
    idComanda = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    #Cada comanda te diferent carretoms
    carretons = models.ManyToManyField(Carreto)
    #la comanda es d'un usuari
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    
    def __str__(self):
        return "{} - {}".format(self.idComanda, self.carretons, self.user)
