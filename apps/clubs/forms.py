from django import forms
from .models import Club

class CreateClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name','description']
        labels = {
            'name': 'Titulo',
            'description': 'Descripcion del club',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingresa un titulo',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    #se puede poner la clase css 'class':texts, o el 'id':'descripcion'
                    'placeholder': 'Ingresa una descripción',
                    'class': 'custom-tinymce',
                }
            ),
        }
        #description = forms.CharField(widget=TinyMCE(attrs={'cols': 40, 'rows': 30, 'class': 'custom-tinymce'}))