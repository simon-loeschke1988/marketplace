from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        # password2 ist das Passwort wiederholen
        #Das sind die Felder die wir im Formular haben wollen
        fields = ['username','email','password1','password2']
    # die Felder im Formular anpassen
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Nutzername',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Deine Mailadresse',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Dein Passwort',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Passwort wiederholen',
        'class':'w-full py-4 px-6 rounded-xl',
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Nutzername',
        'class':'w-full py-4 px-6 rounded-xl',
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Dein Passwort',
        'class':'w-full py-4 px-6 rounded-xl',
    }))