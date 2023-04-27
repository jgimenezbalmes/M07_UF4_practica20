from django.shortcuts import render
import random
from django.http import JsonResponse

# Create your views here.
@api_view(['GET'])
def veure_producte(request, id):
    resposta = Producte.objects.get(idProducte = id)
    serializer = ProducteSerializer(resposta, context={'request': request}, many=True)
    return Response(serializer.resposta)

@api_view(['GET'])
def veure_tots(request):
    resposta = Producte.objects.all()
    serializer = ProducteSerializer(resposta, context={'request': request}, many=True)
    return Response(serializer.resposta)

@api_view(['POST'])
def afegir_producte(request, nomP)