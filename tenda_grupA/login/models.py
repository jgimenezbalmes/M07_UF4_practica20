from django.db import models

# Create your models here.
class User(models.Model):
    idUser = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    mail = models.EmailField()
    password = models.CharField("password", max_length=100)
    userNick = models.CharField("userNick", max_length=12)