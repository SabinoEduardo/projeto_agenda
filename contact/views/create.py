from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact
from django.contrib import messages

# Create your views here.



def create(request):
    """
        Função para criar um contacto
    """
    form_action = reverse('contact:create_contact')

    if request.method == 'POST':

        form = ContactForm(request.POST, request.FILES)
        print(request.POST)

        context = {
            'form' : form,
            'form_action' : form_action
            }
        
        if form.is_valid():
            contact = form.save()
            print('save')
            return redirect(
                'contact:update_contact', 
                contact_id=contact.pk
                )
        
        return render(
                request,
                'contact/create_contact.html', 
                context
                )
    
    context = {
            'form' : ContactForm(),
            'form_action' : form_action
            }
    return render(
        request,
        'contact/create_contact.html', 
        context
    )

# Analisar a viwes que está sendo redirecionada.
 
def update(request, contact_id): 
    """
        Função para atualiar um contacto
    """
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update_contact', args=(contact_id,))
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact,)
        context = {
            'form' : form,
            'form_action' : form_action
            }
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contacto atualizado com sucesso!')
            return redirect('contact:get_contact', contact.id)
        return render(request,'contact/create_contact.html', context)
    context = {
            'form' : ContactForm(instance=contact),
            'form_action' : form_action
            }
    return render(
        request,
        'contact/create_contact.html', 
        context
    )


def delete(request, contact_id): 
    """
        Função para atualiar um contacto
    """
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    confirmation = request.POST.get('confirmation', 'no')
    print('confirmation', confirmation)

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    context = {
        'contact': contact,
        'confirmation':confirmation
        }
    
    return render(request, 'contact/get_contact.html', context)
    
    