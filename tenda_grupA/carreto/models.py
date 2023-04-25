from django.db import models

# Create your models here.
class Carreto(models.Model):
    idCarreto = models.IntegerField(primary_key=True, serialize=True)
    productes = models.ManyToManyField(Producte)

    
