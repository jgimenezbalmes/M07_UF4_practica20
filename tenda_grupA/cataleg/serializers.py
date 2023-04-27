from rest_framework import serializers
from .models import Producte

#Els serializers de Django serveixen per traduir els models a altres formats (JSON, XML,...)
class ProducteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producte
        fields = ('idProducte', 'nom', 'preu', 'fabricant', 'origen', 'caducitat', 'descripcio')