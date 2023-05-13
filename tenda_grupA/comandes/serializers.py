from rest_framework import serializers
from .models import Comanda
from carreto.serializers import CarretoSerializer

#Els serializers de Django serveixen per traduir els models a altres formats (JSON, XML,...)
class ComandaSerializer(serializers.ModelSerializer):
    #Carrega el OBJ de producte i no nomes els ids
    carretons =  CarretoSerializer(many=True)
    class Meta:
        model = Comanda
        fields = ('idComanda', 'user','carretons')