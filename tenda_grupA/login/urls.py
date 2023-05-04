from django.urls import path

from. import views

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_try, name='login'),
    path('home/', views.home, name='home')
]