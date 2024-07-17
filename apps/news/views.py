from django.shortcuts import render
from django.views.generic import ListView
from apps.news.models import News
from .forms import CreateNewsForm
from django.core.paginator import Paginator
# Create your views here.
#Ver video 49-crud para ver form con fechas y selectmultiple

class ListNews(ListView):
    model = News
    form_class = CreateNewsForm
    template_name = 'news/news_list.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
    
    def get_context_data(self,**kwargs):
        context = {}
        context['news'] = self.get_queryset()
        return context
    
    def get(self,request,*args,**kwargs):
        news = self.get_queryset().order_by('-id')
        paginator = Paginator(news,1)
        page = request.GET.get('page')
        news = paginator.get_page(page)
        data = {'news': news, 'form': self.form_class}
        return render(request, self.template_name, data)