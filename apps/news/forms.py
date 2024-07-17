from django import forms
from .models import News

class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','description']
        labels = {
            'title': 'Titulo',
            'description': 'Descripcion de la noticia',
        }
        widgets = {
            'tittle': forms.TextInput(
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