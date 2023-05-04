from django.db import models
from cataleg.models import Producte
# Create your models here.
class Carreto(models.Model):
    idCarreto = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    nomCarreto =  models.CharField("nomCarreto", max_length=50,default=None)
    productes = models.ManyToManyField(Producte)

    
