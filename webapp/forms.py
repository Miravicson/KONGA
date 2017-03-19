from django import  forms
from .models import Person, Order

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        field = ('first_name', 'last_name')