from django.shortcuts import render

# Create your views here.
@api_view(['GET','POST'])
def checkTargeta(nTargeta, dataTargeta, cvc):
    try:
        data = Pagament.objects.get(nTargeta=nTargeta, dataTargeta=dataTargeta, cvc=cvc)
        serializer = PagamentSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data, status="Targeta correcta. Bona compra!")

    except Pagament.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)