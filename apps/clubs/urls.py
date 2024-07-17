from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.static import serve

from django.urls import path, re_path
from . import views


urlpatterns = [
    path('clubs', views.ListClubs.as_view(), name="clubs"),
]
