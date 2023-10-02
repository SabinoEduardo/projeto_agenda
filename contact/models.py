from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

"""
Campos do model
    id (primary key - automático)
    first_name (charfield)
    last_name (charfield)
    phone (charfield)
    email (emailfeed)
    create_date (datafield)
    description (textfield)

    category (foreign key)
    show (boolean)
    owner (foreign key)
    picture (imagefield)

"""

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


   
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True, null=True
        ) # Esse campo serve para inforar o proprietário do contato. Está linkado a clase (model) User do django (from django.contrib.auth.models import User)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = "Cotacto"
        verbose_name_plural = "Contactos"

    