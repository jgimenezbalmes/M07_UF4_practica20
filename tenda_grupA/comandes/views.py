from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Comanda
from .serializers import ComandaSerializer

#View que permet veure una comanda donant el seu id
@api_view(['GET'])
def veure_comanda(request, pk):
    data = Comanda.objects.get(idComanda = pk)
    serializer = ComandaSerializer(data, context={'request': request}, many=False)
    return Response(serializer.data)


#View que permet veure totes les
@api_view(['GET', 'POST'])
def veure_comandes(request):
    if request.method == 'GET':
        data = Comanda.objects.all()
        serializer = ComandaSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ComandaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

