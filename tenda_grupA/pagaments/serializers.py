from rest_framework import serializers
from .models import Pagament

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pagament
        fields = ('idPagament', 'nTargeta', 'dataTargeta', 'cvc')