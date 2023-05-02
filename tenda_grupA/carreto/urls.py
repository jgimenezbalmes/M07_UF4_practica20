from django.urls import path

from. import views

#Dins de carreto, trobem aquestes subrutes
#Els <str:xxx> ens permeten passar parametres a les views
urlpatterns = [
    path('', views.carreto_list, name="llistat"),
    path('id=<str:pk>', views.carreto_id, name="un_producte"),
    path('crear', views.carreto_add_form, name='crear_producto'),
    path('borrar/<str:pk>', views.carreto_delete, name='eliminar_producto'),
    path('modificar/<str:pk>', views.carreto_modify_form, name='actualizar_producto'),
]