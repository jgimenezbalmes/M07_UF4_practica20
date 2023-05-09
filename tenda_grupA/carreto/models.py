from django.db import models
from cataleg.models import Producte
#Importa el User
from login.models import User
# Create your models here.
class Carreto(models.Model):
    idCarreto = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    #nomCarreto =  models.CharField("nomCarreto", max_length=50,default=None)
    productes = models.ManyToManyField(Producte)
    #Per un user te un carreto
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)

    
