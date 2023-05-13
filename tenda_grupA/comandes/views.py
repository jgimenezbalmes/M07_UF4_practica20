from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Comanda, Carreto, User
from .serializers import ComandaSerializer

#View que permet veure una comanda donant el seu id
@api_view(['GET'])
def veure_comanda(request, pk):
    try:
        #Busca la comanda per id
        data = Comanda.objects.get(idComanda = pk)
        serializer = ComandaSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)
    except Comanda.DoesNotExist:
        #Si la comando no existeix
        return Response(status=status.HTTP_404_NOT_FOUND)



#View que permet veure totes les comandes
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

#Crea una comanda
@api_view(['GET', 'POST'])
def comanda_add(request, carretonsC, userC):
    carretonsList = [int(e) for e in carretonsC.split(",")]
    myUser = User.objects.get(idUser = userC)
    com = Comanda(user=myUser)
    com.save()
    com.carretons.set(carretonsList)
    return Response({'success': 'Comanda creada'}, status=status.HTTP_201_CREATED)


#Crea una comanda
@api_view(['GET', 'DELETE'])
def comanda_borrar(request, idC):
    prod = Comanda.objects.filter(idComanda=idC)
    prod.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#Crea una comanda
@api_view(['GET', 'PUT'])
def comanda_modify(request, comId, carretonsC):
    #Mira si existeix la comanda
    try:
        com = Comanda.objects.get(idComanda=int(comId))
        #Fa un llistat de les comandes passades
        comandesList = [int(e) for e in carretonsC.split(",")]
        myComandes = Carreto.objects.filter(idCarreto__in=comandesList)
        com.save()
        com.carretons.set(myComandes)
        serializer = ComandaSerializer(com, context={'request': request})
        return Response(serializer.data)
    except Comanda.DoesNotExist:
        #Sino retorna error
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
#Mostra el historial de un usuari
def comanda_user(request, idC):
    try:
        #Busca el usuari per aquest id
        myUser = User.objects.get(idUser = int(idC))
        #Filtra la comanda per aquest user
        myComanda = Comanda.objects.filter(user=myUser).first()
        print("pedrolo {}".format(myComanda))
        serializer = ComandaSerializer(myComanda, context={'request': request}, many=False)
        return Response(serializer.data)

    except User.DoesNotExist:
        #Si la comando no existeix
        return Response(status=status.HTTP_404_NOT_FOUND)
