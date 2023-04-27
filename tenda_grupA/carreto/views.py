from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#Importamos models
from .models import Producte, Carreto
from .serializers import *
from django.http import JsonResponse



@api_view(['GET', 'POST'])
def catalegs_list(request):
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
def cataleg_id(request, pk):
    try:  
        data = Carreto.objects.get(idCarreto=pk)
        serializer = CarretoSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
