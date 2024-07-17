from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ContactUsForm, CreateEventForm
from .models import Event, ContactUs
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.template.loader import render_to_string

import matplotlib.pyplot as plt
import io
import urllib, base64

# Create your views here.
'''
Cuando se utiliza view primero se ejecuta dispatch() encargado de identificar el metodo, luego se ejecuta
http_method_not_allowed() cuando dispatch no se encuentra y es un metodo no soportado, luego options() cuando
se ejecuta el metodo options.

Todas las vstas genericas heredan de view
View se usa cuando se va a tener algo de logica
TemplateView cuando solo se va renderizar un template y solo se usara metodo get (solo tiene definido get)
ListView vista para listar su queryset, por defecto hace Model.objects.all() por defecto envia la consulta al template con nombre objects_list
UpdateView vista para actualiza algun objeto de modelo, en la url debe estar como pk no id, reverse_lazy es alternativa a redirect, se usa no como retorno sino como accion terminada de manera mas formal, solo funciona cuando no se sobreescribe o edita la informacion
en el template se define como form.nombre.label, form.nombre
DeleteView se usa para eliminar objetos, no funciona reverse_lazy en eliminacion lógica
'''

class Home(TemplateView):
    template_name = 'index.html'
    def get(self,request,*args,**kwargs):
        queryset = request.GET.get("buscar")
        if queryset: Event.objects.filter(
            Q(tittle=queryset) |
            Q(type=queryset)
        ).distinct()
        return render(request, self.template_name)


class CreateContact(CreateView):
    template_name = 'contact.html'
    model = ContactUs
    form_class = ContactUsForm
    success_url = reverse_lazy('home')


class CreateEvent(CreateView):
    template_name = 'events/create_event.html'
    model = Event
    form_class = CreateEventForm
    success_url = reverse_lazy('events')

    def post(self,request,*args,**kwargs): #es necesario que el form html no tenga un action para que django llame la misma ruta y ejecute el metodo
        form = self.form_class(request.POST, request.FILES)
        print(form.is_valid())
        print(form.errors)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events')
        events = self.get_queryset().order_by('-id')
        paginator = Paginator(events, 1)
        page = request.GET.get('page')
        events = paginator.get_page(page)
        data = {'events': events, 'form': form}
        return render(request, self.template_name, data)
    

class CreateEventModal(CreateView):
    template_name = 'partials/_create_event_modal.html'
    model = Event
    form_class = CreateEventForm
    success_url = reverse_lazy('events')

    def form_invalid(self, form):
        form_html = render_to_string(self.template_name, {'form': form}, request=self.request)
        return JsonResponse({'success': False, 'form_html': form_html})

    def form_valid(self, form):
        event = form.save()
        event_html = render_to_string('partials/_event.html', {'event': event}, request=self.request)
        return JsonResponse({'success': True, 'event_html': event_html, 'event_id': event.id})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class UpdateEvent(UpdateView):
    template_name = 'partials/_event_modal.html'
    model = Event
    form_class = CreateEventForm
    success_url = reverse_lazy('events')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        context['events'] = Event.objects.filter(is_active=True,pk=id)
        return context

class DeleteEvent(DeleteView):
    model = Event
    template_name = 'events/delete_event.html'

    def post(self,request,pk,*args,**kwargs):
        event = Event.objects.get(pk = pk)
        event.is_active = False
        event.save()
        return redirect('events')


class EventDetail(DetailView):
    model = Event
    template_name = 'events/event_detail.html'


#ListView aunque soporta el metodo post no fue creado con ese proposito, principalmente para get
#View no crea un metodo get automaticamente, unicamente si se define
class EventList(View):
    model = Event
    #template_name = 'events/event_list.html'
    #context_object_name = 'events'
    #paginate_by = 1
    form_class = CreateEventForm
    template_name = 'events/event_list.html'

    #queryset = Event.objects.filter(is_active=True)
    #def get_queryset(self): Internamente Django ejecuta este metodo y ejecuta la consulta definida en queryset
        #print('Mensaje desde queryset')
        #self.queryset = self.model.objects.all()
        #return self.queryset
    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
    
    #de manera similar a get_queryset funciona con el contexto
    def get_context_data(self,**kwargs):
        context = {}
        context['events'] = self.get_queryset()
        return context
    
    def get(self,request,*args,**kwargs):
        # Por defecto cuando solo se pone el modelo es Event.objects.all() con nombre object_list
        events = self.get_queryset().order_by('-id')
        paginator = Paginator(events,12)
        page = request.GET.get('page')
        events = paginator.get_page(page)
        data = {'events': events, 'form': self.form_class}
        return render(request, self.template_name, data)


class Loading(TemplateView):
    template_name = 'loading.html'



'''Mixins permiten colocar codigo que permite hacer alguna validacion, poner informacion extra, pero poder globalizarla o generalizarla
para muchas clases, es utilizado para validaciones de usuario, permisos
Mixin=Mezcla de funciones o acciones que queremos que se realicen para la clase en la que se agrega
    
Existen tres formas de proteger las rutas o codigo para que pida que el usuario este logueado

1. Login required en la url y englobar la clase o metodo
2. decorador @method_decorator(login_required) pide el inicio de sesion a la funcion, es solo para funciones
3. utilizando mixins, el de django se llama LoginRequiredMixin se importa de django.contrib.auth.mixins
   se agrega en las clase que hereda, y debe haber gerarquia entonces va de primeras, por que es lo primero que se quiere

'''