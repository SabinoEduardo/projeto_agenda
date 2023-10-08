from typing import Any
from contact.models import Contact
from django.core.exceptions import ValidationError
from django import forms
from contact.widgets import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class ContactForm(forms.ModelForm):

    first_name = first_name
    last_name = last_name
    phone = phone
    email = email
    picture = picture
    """
        Classe usada para criada um fómulário para contacto
    """
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category',
                  'picture',)

        
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        
        if last_name == first_name:
            msg = ValidationError(
                    'O primeiro nome não pode ser igual ao segund', code='invalid'
                )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        return super().clean()
        
        # Aqui estamos adicionando mensagem de erro fora de um campo
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
         
        if first_name == 'ABC':
            self.add_error('first_name', 
                ValidationError(
                    'Mensagem de Erro 2', code='invalid'
                )
            )
        return first_name
    
class  RegisterUser(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
      
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Já existe este email', code='invalid'
                )
            )
        return email
        
