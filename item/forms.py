from django import forms 
from .models import Item

INPUT_CLASSES = 'w-full  py-4 px-6 rounded-xl border'
'''KLASSEN FÜR DIE FORMULARE'''
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','description','price','category','image']
        
        # Hier eine andere Art, Formulare zu erstellen
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES}),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES}),
        }
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','description','price','image','is_sold']
        
        # Hier eine andere Art, Formulare zu erstellen
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES}),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES}),
        }