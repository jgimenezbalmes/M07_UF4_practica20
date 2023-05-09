from django.db import models

# Create your models here.
class Pagament(models.Model):
    #auto_created fa que s'autogeneri l'id quan es crea un nou objecte Pagament a la taula.
    idPagament = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    #Fiquem un BigInteger ja que el Integer normal no permet que fiquem un numero tan gran com el de la targeta
    nTargeta = models.BigIntegerField()
    dataTargeta = models.DateField()
    cvc = models.IntegerField(max_length=3)

