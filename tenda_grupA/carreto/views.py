from django.shortcuts import render,redirect

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#Importamos models
from .models import Producte, Carreto
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
    
#funcoio que es crida per afegir un carreto
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

#funcio que es crida per modificar un carreto
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

#funcio que es crida per eliminar un carreto
@api_view(['GET','DELETE'])
def carreto_delete(request,pk):
    #Context del formulari
    try:
        carreto = Carreto.objects.get(idCarreto = pk)
        carreto.delete()
        return render(request,'carreto_ok.html')   
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    



