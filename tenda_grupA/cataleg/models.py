from django.db import models

# Create your models here.
class Producte(models.Model):
    idProducte = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    nom = models.IntegerField()
    preu = models.DecimalField()
    fabricant = models.CharField("fabricant", max_length=50)
    origen = models.CharField("fabricant", max_length=50)
    caducitat = models.DateField()
    descripcio = models.TextField()

