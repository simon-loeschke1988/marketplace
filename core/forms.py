from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        # password2 ist das Passwort wiederholen
        #Das sind die Felder die wir im Formular haben wollen
        fields = ['username','email','password1','password2']
        
