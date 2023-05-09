from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PagamentSerializer
from .models import Pagament



# Create your views here.

#View que agafa un numero de targeta, una data de caducitat i un cvc. Retorna missatge d'exit si existeix la combinacio de dades,
#i retorna un missatge d'error si aquesta no existeix
@api_view(['GET','POST'])
def checkTargeta(request, nTargeta, dataTargeta, cvc):
    try:
        #Agafem l'objecte Pagament que compleix aquest nTargeta, data i cvc
        data = Pagament.objects.get(nTargeta=nTargeta, dataTargeta=dataTargeta, cvc=cvc)
        #Si l'objecte reclamat existeix, retorna un status 302 amb un missatge confirmant la compra
        return Response( {"Compra amb exit": "Targeta correcta! Bona compra!"}, status=status.HTTP_302_FOUND)

    #En cas que no existeixi l'objecte Pagament reclamat, enviara el següent missatge d'error amb un codi 404
    except Pagament.DoesNotExist:
        return Response({"Error": "Targeta no trobada. Torna a introduïr les dades"}, status=status.HTTP_404_NOT_FOUND)

