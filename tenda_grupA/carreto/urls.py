from django.urls import path

from. import views
#Dins de carreto, trobem aquestes subrutes
#Els <str:xxx> ens permeten passar parametres a les views
urlpatterns = [
    path('', views.carreto_list, name="llistat"),
    path('id=<str:pk>', views.carreto_id, name="un_producte"),
    #path('crear', views.carreto_add_form, name='crear_producto'),
    path('crear/productes=<str:productesC>&user=<str:userC>', views.carreto_add, name="afegir_carreto"),
    path('borrar/id=<str:pk>', views.carreto_delete, name='eliminar_carreto'),
    #path('modificar/<str:pk>', views.carreto_modify_form, name='actualizar_producto'),
    path('modificar/idCarreto=<str:idC>&productes=<str:productesC>&user=<str:userC>', views.carreto_modify, name="modificar_carreto")
]