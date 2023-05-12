from django.urls import path

from. import views

#Dins de cataleg, trobem aquestes subrutes
#Els <str:xxx> ens permeten passar parametres a les views
urlpatterns = [
    path('', views.veure_comandes, name="lista_comandes"),
    path('<str:pk>', views.veure_comanda, name="una_comanda")
    #path('crear/<str:nomP>&<str:preuP>&<str:fabP>&<str:origenP>&<str:cadP>&<str:descP>', views.add_comanda, name="add_comanda"),
    #path('borrar/<str:idP>', views.elimina_producte, name="elimina_producte"),
    #path('modificar/<str:idP>&<str:nomP>&<str:preuP>&<str:fabP>&<str:origenP>&<str:cadP>&<str:descP>', views.update_comanda, name="update_comanda")
]