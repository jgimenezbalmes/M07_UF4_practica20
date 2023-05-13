from django.urls import path

from. import views

#Dins de cataleg, trobem aquestes subrutes
#Els <str:xxx> ens permeten passar parametres a les views
urlpatterns = [
    path('', views.veure_comandes, name="lista_comandes"),
    path('id=<str:pk>', views.veure_comanda, name="una_comanda"),
    path('crear/carretons=<str:carretonsC>&user=<str:userC>', views.comanda_add, name="add_comanda"),
    path('borrar/id=<str:idC>', views.comanda_borrar, name="elimina_comanda"),
    path('modificar/id=<str:comId>&carretons=<str:carretonsC>', views.comanda_modify, name="update_comanda"),
    path('historial/user=<str:idC>', views.comanda_user, name="historial_user")
]