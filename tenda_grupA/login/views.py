from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User

@api_view(['GET', 'POST'])
def login_try(request):
    if request.method == 'POST':
        # Retrieve the username and password from the login form
        identificador = request.POST['mail']
        passwd = request.POST['password']

        # Check whether the username is an email or a nickname
        if '@' in identificador:
            # Check for the user by email
            try:
                user = User.objects.get(mail=identificador, password=passwd)
            except User.DoesNotExist:
                user = None
        else:
            # Check for the user by nickname
            try:
                user = User.objects.get(userNick=identificador, password=passwd)
            except User.DoesNotExist:
                user = None

        # If the user exists, log them in and redirect to the home page
        if user is not None:
            # You may want to customize this logic based on how you've implemented authentication in your project
            # Here, we're simply setting a session variable to indicate that the user is logged in
            request.session['userNick'] = user.userNick
            return redirect('home')
        else:
            # If the user does not exist, render the login page with an error message
            context = {'error_message': 'Usuari, mail o contrasenya erronis'}
            return render(request, 'login/login.html', context)

    else:
        # If the request method is GET, render the login page
        context = {'error_message': 'Usuari, mail o contrasenya erronis'}
        return render(request, 'login/login.html', context)



def home(request):
    # Retrieve the user's email from the session
    user_nick = request.session.get('userNick')

    # If the user is not logged in, redirect to the login page
    if not user_nick:
        return redirect('login')

    # Otherwise, render the home page with the user's email
    return render(request, 'login/home.html', {'user_nick': user_nick})

