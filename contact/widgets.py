from django import forms

first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Digite seu Primeiro Nome'
            }
        ),
        label = 'Primeiro Nome',
        help_text='Primeiro nome'
        )

last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Digite seu Sobrenome'
            }
        ),
        label = 'Sobrenome',
        help_text='Último nome'
        )

phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Digite o número do celular'
            }
        ),
        label = 'Celular',
        )

email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Digite seu e-mail'
            }
        ),
        label = 'E-mail',
        )

picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={'accept':'image/*'}, 
            ),
        required=False
        )
