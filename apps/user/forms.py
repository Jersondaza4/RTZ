from django.contrib.auth.forms import AuthenticationForm
from django import forms
from apps.user.models import User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Nombre de usuario'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'
        

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs = {
            #'class': 'class',
            'placeholder': 'ingrese su contraseña',
            'id': 'password1',
            'required':'required',
        }
    ))
    password2 = forms.CharField(label='Contraseña de confirmación', widget=forms.PasswordInput(
        attrs = {
            #'class': 'class',
            'placeholder': 'ingrese nuevamente su contraseña',
            'id': 'password2',
            'required':'required',
        }
    ))

    class Meta:
        model = User
        fields = ('email','username','names','last_names')
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'placeholder': 'correo',
                }
            ),
            'names': forms.TextInput(
                attrs = {
                    'placeholder': 'ingrese sus nombres',
                }
            ),
            'last_names': forms.TextInput(
                attrs = {
                    'placeholder': 'ingrese sus apellidos',
                }
            ),
            'username': forms.TextInput(
                attrs = {
                    'placeholder': 'ingrese sus nombre de usuario',
                }
            )
        }

    def clean_password2(self):
        '''
        Validacion de que ambas contraseñas sean iguales inicia por clean antes de ser encriptadas y guardadas
        excepcion: Validation error cuando las contraseñas no son iguales muestra mensaje de error
        cleaned data, se hace clic en el boton de submit, la informacion llega a django se guarda en una variable y luego se valida (is_valid), si es valida se guarda
        el metodo is_valid llama una serie de metodos si no se define ninguna solo hace las de base de datos
        una vez validados los datos los pasa a un diccionario llamado cleaned_data que es la información ya lista para usarse
        como es un diccionario tiene el metodo get para extraer informacion a traves de su key
        '''
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2
    

    def save(self,commit =True):
        '''cuando se usa form.save() se esta llamando al metodo save de forms de django, commit es que proceda con el registro
            super() es el contructor interno que tiene la clase
            commit = FAlse para guardar la instancia
            se realiza el guardado del formulario
        '''
        user = super().save(commit=False)
        user.set_password(self.cleaned_data('password1'))
        if commit:
            user.save()
        return user
