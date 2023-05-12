from rest_framework import serializers
from .models import Comanda

#Els serializers de Django serveixen per traduir els models a altres formats (JSON, XML,...)
class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = ('idProducte', 'nom', 'preu', 'fabricant', 'origen', 'caducitat', 'descripcio')