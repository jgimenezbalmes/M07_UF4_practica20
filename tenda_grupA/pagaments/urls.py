from django.urls import path

from. import views

from django.urls import path
from . import views

urlpatterns = [
    path('ntarg=<str:nTargeta>&data=<str:dataTargeta>&cvc=<str:cvc>', views.checkTargeta, name='check')
]