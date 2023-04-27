from rest_framework import serializers
from .models import Producte

class ProducteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producte
        fields = ('idProducte', 'nom', 'preu', 'fabricant', 'origen', 'caducitat', 'descripcio')