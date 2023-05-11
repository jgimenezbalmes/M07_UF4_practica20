from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User

@api_view(['GET', 'POST'])
def login_try(request):

    context = {}

    if request.method == 'POST':
        # S'agafa el mail i el password 
        identificador = request.POST['mail']
        passwd = request.POST['password']

        # Es guarda l'usuari de la taula usuari que te el mail i contrassenya passats
        try:
            user = User.objects.get(mail=identificador, password=passwd)
            #Si no existeix, l'usuari es guarda com a None
        except User.DoesNotExist:
            user = None

        # Si l'usuari no es Null...
        if user is not None:
            #Es guarda a la sessió el nick de l'usuari aconseguit
            request.session['userNick'] = user.userNick
            #Es redirigeix a la url de home
            return redirect('home')
        else:
            #Si l'usuari no existeix, es passa un missatge d'error i es torna a carregar la pagina de login.
            context = {'error_message': 'Usuari, mail o contrasenya erronis'}
            return render(request, 'login/login.html', context)

    else:
        #Si no es fes post, es carrega el template (de normal aixo es a l'inici)
        return render(request, 'login/login.html', context)



def home(request):
    # S'agafa el nick guardat al view anterior
    user_nick = request.session.get('userNick')

    # Si no es troba, es redirigeix al login
    if not user_nick:
        return redirect('login')

    # Si sí es troba es fa render del template de home, passant el nick de l'usuari
    return render(request, 'login/home.html', {'user_nick': user_nick})

