from rest_framework import serializers

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Carreto
from .serializers import *

class CarretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreto
        fields = ('idCarreto', 'nomCarreto','productes')



    