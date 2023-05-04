from django.db import models

# Create your models here.
class Producte(models.Model):
    #El id es genera sol, es incrementable i es clau primaria
    idProducte = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    nom = models.CharField("nom", max_length=50)
    #El camp decimal requereix determinar un numero de digits maxims, i un numero de decimals
    preu = models.DecimalField(max_digits=10, decimal_places=2)
    fabricant = models.CharField("fabricant", max_length=50)
    origen = models.CharField("origen", max_length=50)
    #El format de data es YYYY-MM-DD
    caducitat = models.DateField()
    descripcio = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.idProducte, self.nom)