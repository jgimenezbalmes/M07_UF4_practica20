from django.shortcuts import render

# Create your views here.
@api_view(['GET', 'POST'])
def users_agafaun(request, identificador, passwd):
    try:
        #Si te un @, sera un mail. Sino sera un nickname
        if '@' in identificador:
            #Mirar per email
            data = User.objects.get(mail=identificador, password=passwd)
        else:
            #Mirar per nickname
            data = User.objects.get(userNick=identificador, password=passwd)

        serializer = UserSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
