from django.urls import path

from. import views


urlpatterns = [
    path('', views.veure_tots, name="llistat"),
    path('<str:pk>', views.veure_producte, name="un_producte"),
    path('crear/<str:nomP>&<str:preuP>&<str:fabP>&<str:origenP>&<str:cadP>&<str:descP>', views.afegir_producte, name="afegir_producte"),
    path('borrar/<str:idP>', views.elimina_producte, name="elimina_producte"),
    path('modificar/<str:idP>&<str:nomP>&<str:preuP>&<str:fabP>&<str:origenP>&<str:cadP>&<str:descP>', views.actualitzar_producte, name="actualitzar_producte")
]