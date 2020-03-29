from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser/', views.add_user_view, name='addUser'),
    path('publicos/<slug:username>',
         views.get_portafolios_publicos, name='publicos'),
    path('login/', views.iniciar_sesion, name='login'),
    path('actualizarUsuario/', views.actualizar_usuario, name='editUser')



]
