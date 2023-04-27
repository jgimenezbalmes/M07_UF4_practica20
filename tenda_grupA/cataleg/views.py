from django.shortcuts import render
import random
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Producte
from .serializers import ProducteSerializer

# Create your views here.
@api_view(['GET'])
def veure_producte(request, pk):
    data = Producte.objects.get(idProducte = pk)
    serializer = ProducteSerializer(data, context={'request': request}, many=False)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def veure_tots(request):
    if request.method == 'GET':
        data = Producte.objects.all()
        serializer = ProducteSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProducteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def afegir_producte(request, nomP, preuP, fabP, origenP, cadP, descP):
    prod= Producte(nom = nomP, preu= preuP, fabricant=fabP, origen=origenP, caducitat=cadP, descripcio=descP)
    prod.save()
    return Response({'success': 'Producte creat amb exit.'}, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def actualitzar_producte(request, idP, nomP, preuP, fabP, origenP, cadP, descP):
    try:
        prod = Producte.objects.get(idProducte=idP)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    prod.nom = nomP
    prod.preu = preuP
    prod.fabricant = fabP
    prod.origen = origenP
    prod.caducitat = cadP
    prod.descripcio = descP
    prod.save()
    serializer = ProducteSerializer(prod, context={'request': request})

    return Response(serializer.data)

@api_view(['DELETE'])
def elimina_producte(request, idP):
    prod = Producte.objects.filter(idProducte=idP)
    prod.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
