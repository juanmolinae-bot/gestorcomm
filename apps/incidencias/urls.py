from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('', views.dashboard, name='dashboard'),
    path('incidencias/', views.lista_incidencias, name='lista_incidencias'),
    path('incidencias/nueva/', views.crear_incidencia, name='crear_incidencia'),
    path('incidencias/<int:pk>/', views.detalle_incidencia, name='detalle_incidencia'),
    path('incidencias/<int:pk>/editar/', views.editar_incidencia, name='editar_incidencia'),
    path('incidencias/<int:pk>/eliminar/', views.eliminar_incidencia, name='eliminar_incidencia'),
]
