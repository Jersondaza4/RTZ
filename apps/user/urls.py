from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('init-list-user', login_required(views.InitListUser.as_view()), name="init_list_user"),
    path('list-user', login_required(views.ListUser.as_view()), name="user_list"),
    path('create-user', login_required(views.RegisterUser.as_view()), name="create_user"),
    path('update-user/<int:pk>', login_required(views.UpdateUser.as_view()), name="update_user"),
    path('delete-user/<int:pk>', login_required(views.DeleteUser.as_view()), name="delete_user"),
]

#URL DE VISTAS IMPLICITAS
'''
urlpatterns += [
    path('init-list-user', login_required(
        TemplateView.as_view(
            template_name='users/list_user.html'
        )
    ), name="init_list_user"),
]'''