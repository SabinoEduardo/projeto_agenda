from contact.forms import RegisterUser
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def create_user(request):
    form = RegisterUser()

    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado com sucesso!")  
            return redirect('contact:index')  
    return render(
        request,
        'contact/create_user.html',
        {
            'form' : form
        }
        )

def login_user(request): # continuar aqui, criando _login de user
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            # messages.success(request, "Usuário criado com sucesso!")  
            return redirect('contact:index')  
    return render(
        request,
        'contact/create_user.html',
        {
            'form' : form
        }
        )


