from django.db import models

# Create your models here.
class Pagament(models.Model):
    idPagament = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    nTargeta = models.IntegerField()
    dataTargeta = models.DateField()
    cvc = models.IntegerField(max_length=3)

