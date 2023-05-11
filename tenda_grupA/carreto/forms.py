from django.forms import ModelForm
from .models import Carreto

#Es crea un formulari segons el OBJ 'Student'
class CarretoForm(ModelForm):
    class Meta:
        model = Carreto
        #field = Student -> name, age
        fields = '__all__'

