from django.shortcuts import render
from django.views.generic import ListView
from apps.clubs.models import Club
from .forms import CreateClubForm
from django.core.paginator import Paginator
# Create your views here.
#Ver video 49-crud para ver form con fechas y selectmultiple

class ListClubs(ListView):
    model = Club
    form_class = CreateClubForm
    template_name = 'clubs/clubs_list.html'

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self,**kwargs):
        context = {}
        context['news'] = self.get_queryset()
        return context
    
    def get(self,request,*args,**kwargs):
        clubs = self.get_queryset().order_by('-id')
        paginator = Paginator(clubs,4)
        page = request.GET.get('page')
        clubs = paginator.get_page(page)
        data = {'clubs': clubs, 'form': self.form_class}
        return render(request, self.template_name, data)