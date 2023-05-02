from django.urls import path

from. import views

urlpatterns = [
path('login/<str:identificador>&<str:passwd>', views.users_agafaun, name="un_producte")
]