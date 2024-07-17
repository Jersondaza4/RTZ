from django import forms
from .models import ContactUs, Event
from tinymce.widgets import TinyMCE


# Code added for loading form data on the Booking page
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"   


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['tittle','description','event_date','place','type','image']
        labels = {
            'tittle': 'Titulo',
            'description': 'Descripcion del evento',
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
        