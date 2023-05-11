from django.db import models
from cataleg.models import Producte
from login.models import User
# Create your models here.
class Carreto(models.Model):
    idCarreto = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    productes = models.ManyToManyField(Producte)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    
