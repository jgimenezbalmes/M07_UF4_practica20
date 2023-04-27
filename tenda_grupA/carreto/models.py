from django.db import models
from cataleg.models import Producte
# Create your models here.
class Carreto(models.Model):
    idCarreto = models.IntegerField(primary_key=True, serialize=True)
    productes = models.ManyToManyField(Producte)

    
