from django.db import models
from cataleg.models import Producte
from login.models import User
# Create your models here.
class Carreto(models.Model):
    idCarreto = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    productes = models.ManyToManyField(Producte)
    #El user el porta Comanda
    #user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    #Quan creas carretons, no son comprats i per ara no son de cap usuari
    esComprat = models.BooleanField(default=False)

    
