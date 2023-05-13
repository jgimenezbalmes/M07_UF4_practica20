from rest_framework import serializers

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Carreto
from .serializers import *
from cataleg.serializers import ProducteSerializer

class CarretoSerializer(serializers.ModelSerializer):
    #Carrega el OBJ de producte i no nomes els ids
    productes =  ProducteSerializer(many=True)
    class Meta:
        model = Carreto
        fields = ('idCarreto','esComprat', 'productes')
    

    