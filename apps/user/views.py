import json
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView, CreateView, UpdateView, DeleteView, ListView, TemplateView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm, UserForm
from .models import User
from apps.user.mixins import LoginAndSuperUserMixin, ValidateRequiredPermissionsMixin
# Create your views here.

class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, **kwargs)
        
    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)
    

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class RegisterUser(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('user:user_list')

    def post(self,request,*args,**kwargs):
        ''' De esta manera no se valida post por que ya se reescribe
        en vez de llamar al metodo save del formulario se crea una instancia para encriptar la contraseña
        luego s ellama al metodo save pero del modelo
        sirve para validr informacion enviada de un form de django a traves de una peticion AJAX
        para usar las validaciones de django con cleaned_data
        Se realiza el guardado del modelo
        '''
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = User(
                email= form.cleaned_data.get('email'),
                username= form.cleaned_data.get('username'),
                names= form.cleaned_data.get('names'),
                last_names= form.cleaned_data.get('last_names'),
            )
            new_user.set_password(form.cleaned_data.get('password1'))
            new_user.save()
            return redirect('user:user_list')
        else:
            return render(request,self.template_name,{'form':form})
        

class InitListUser(LoginAndSuperUserMixin,ValidateRequiredPermissionsMixin,TemplateView):
    permission_required = ('user.view_user','user.add_user')
    template_name = 'users/list_user.html'


class ListUser(ListView):
    model = User
    template_name = 'users/list_user.html'
    
    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
    
    #Forma manual de manejar la solicitud ajax
    '''def get(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': #verifica si es ajax
            list_users=[]
            for user in self.get_queryset():
                data_user={}
                data_user['id']=user.id
                data_user['names']=user.names
                data_user['last_names']=user.last_names
                data_user['email']=user.email
                data_user['username']=user.username
                data_user['is_active']=user.is_active
                list_users.append(data_user)
            data = json.dumps(list_users)
            return HttpResponse(data,'application/json')
        else:
            return render(request,self.template_name)'''
    
    #serialize, serializar representa convertir la información de un tipo a otro tipo
    def get(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': #verifica si es ajax
            data = serialize('json',self.get_queryset()) #solo funciona con filter, no con get del get_queryset (solo varios elementos)
            return HttpResponse(data,'application/json')
        else:
            return render(request,self.template_name)


class DeleteUser(DeleteView):
    model = User


class UpdateUser(UpdateView):
    model = User
    form_class = UserForm

