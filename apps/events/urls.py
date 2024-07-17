from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.static import serve

from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('contact', views.CreateContact.as_view(), name="contact"),
    path('events', views.EventList.as_view(), name="events"),
    path('create-event', login_required(views.CreateEvent.as_view()), name="create_event"),
    path('create-event-modal', login_required(views.CreateEventModal.as_view()), name="create_event_modal"),
    path('event/<int:pk>', login_required(views.EventDetail.as_view()), name="event_detail"),
    path('update-event/<int:pk>', login_required(views.UpdateEvent.as_view()), name="update_event"),
    path('delete-event/<int:pk>', login_required(views.DeleteEvent.as_view()), name="delete_event"),
    path('loading/', views.Loading.as_view(), name='loading'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^uploads/(?P<path>.*)$',serve,{
    'document_root': settings.MEDIA_ROOT,
    })
]