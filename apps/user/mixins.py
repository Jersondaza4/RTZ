#Validar si un usuario es superusuario
#object, raiz de donde heredan todas las clases de python

from django.shortcuts import redirect
from django.urls import reverse_lazy

class LoginAndSuperUserMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')
    

class ValidateRequiredPermissionsMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required,str):
            return (self.permission_required)
        return self.permission_required
    
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('index')
        return self.url_redirect
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request,*args,**kwargs)
        return redirect(self.get_url_redirect())