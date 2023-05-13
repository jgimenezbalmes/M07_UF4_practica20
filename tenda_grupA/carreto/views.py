from django.shortcuts import render,redirect

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#Importamos models
from login.models import User
from cataleg.models import Producte
from carreto.models import Carreto

from .serializers import *
from django.http import JsonResponse

from .forms import CarretoForm


@api_view(['GET', 'POST'])
def carreto_list(request):
    if request.method == 'GET':
        data = Carreto.objects.all()
        serializer = CarretoSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CarretoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def carreto_id(request, pk):
    try:  
        data = Carreto.objects.get(idCarreto=pk)
        serializer = CarretoSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
#funcoio que es crida per afegir un carreto FORMULARI
@api_view(['GET', 'POST'])
def carreto_add_form(request):
    form = CarretoForm(request.POST)
    #Context del formulari
    context = {'forms':form}
    if request.method == 'POST':
        #Si es un metode post i el valid, envia el formulari
        if form.is_valid():
            #Si es valid l'envia
            form.save()
            #Redirecciona al template
            return render(request,'carreto_ok.html',context)
    return render(request,'form.html',context)


@api_view(['GET', 'POST'])
def carreto_add(request, productesC):
    #Fa una llista dels ids de productes
    productesList = [int(e) for e in productesC.split(",")]
    myProducts = Producte.objects.filter(idProducte__in=productesList)
    #Un carreto per defecte no es comprat
    carr = Carreto(esComprat=False)
    carr.save()
    carr.productes.set(myProducts)
    return Response({'success': 'Carreto creat'}, status=status.HTTP_201_CREATED)

#funcio que es crida per modificar un carreto FORMULARI
@api_view(['GET', 'PUT','POST'])
def carreto_modify_form(request,pk):
  #Agafa les dades del 'carreto' en concret
    carreto = Carreto.objects.get(idCarreto = pk)
    form = CarretoForm(instance=carreto)
    #Context del formulari
    context = {'forms':form}
    if request.method == 'POST':
        form = CarretoForm(request.POST, instance=carreto)
    if form.is_valid():
        #Guarda els canvis
        form.save()
        #Redirecciona al template
        return render(request,'carreto_ok.html',context)
    return render(request,'form.html',context)

#funcio que es crida per modificar un carreto
@api_view(['GET','PUT'])
def carreto_modify(request, idC, productesC):
    #Mira si existeix el carreto
    try:
        prod = Carreto.objects.get(idCarreto=int(idC))
        #Fa un llistat dels productes passats
        productesList = [int(e) for e in productesC.split(",")]
        #Aconsegueix els productes per id
        myProducts = Producte.objects.filter(idProducte__in=productesList)
        prod.save()
        prod.productes.set(myProducts)
        serializer = CarretoSerializer(prod, context={'request': request})
        return Response(serializer.data)
    except Carreto.DoesNotExist:
        #Sino retorna error
        return Response(status=status.HTTP_404_NOT_FOUND)


#funcio que es crida per eliminar un carreto
@api_view(['GET','DELETE'])
def carreto_delete(request, pk):
    #Esborra el carreto a partir de una id
    try:
        carreto = Carreto.objects.get(idCarreto = pk)
        carreto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    


#funcio que es crida per modificar un carreto
@api_view(['GET','PUT'])
def carreto_pagar(request, idC):
    #Agafa el Carreto per id
    try:  
        carr = Carreto.objects.get(idCarreto=idC)
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #Si el producte
    if carr.esComprat == True:
        #Si ja l'has pagat no et deixa tornar a pagar
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        #El marca com a pagat
        carr.esComprat = True
        carr.save()
        serializer = CarretoSerializer(carr, context={'request': request}, many=False)
        return Response(serializer.data)