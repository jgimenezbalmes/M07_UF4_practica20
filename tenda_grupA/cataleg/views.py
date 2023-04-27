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
