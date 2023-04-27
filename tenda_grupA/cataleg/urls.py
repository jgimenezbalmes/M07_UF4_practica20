from django.urls import path

from. import views


urlpatterns = [
    path('', views.veure_tots, name="llistat"),
    path('<str:pk>', views.veure_producte, name="un_producte"),
    path('crear/', views.afegir_producte, name="afegir_producte"),
    path('borrar/<str:pk>', views.elimina_producte, name="elimina_producte"),
    path('modificar/<str:pk>', views.actualitzar_producte, name="actualitzar_producte")
]