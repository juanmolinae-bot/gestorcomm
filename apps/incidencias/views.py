from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Incidencia, Zona
from .forms import LoginForm, IncidenciaForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
    else:
        form = LoginForm()
    return render(request, 'incidencias/login.html', {'form': form})


def logout_view(request):
    """Vista de logout. Acepta GET y POST.
    Para GET muestra una pantalla de confirmacion (resuelve la observacion
    de la entrega anterior sobre como cerrar sesion).
    """
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'incidencias/logout_confirm.html')


@login_required
def perfil(request):
    """Pantalla de perfil con boton de cerrar sesion (mejora semana 11)."""
    return render(request, 'incidencias/perfil.html', {'usuario': request.user})


@login_required
def dashboard(request):
    incidencias = Incidencia.objects.all()[:5]
    total_abiertas = Incidencia.objects.filter(estado='abierta').count()
    total_revision = Incidencia.objects.filter(estado='en_revision').count()
    total_cerradas = Incidencia.objects.filter(estado='cerrada').count()
    contexto = {
        'incidencias_recientes': incidencias,
        'total_abiertas': total_abiertas,
        'total_revision': total_revision,
        'total_cerradas': total_cerradas,
    }
    return render(request, 'incidencias/dashboard.html', contexto)


@login_required
def lista_incidencias(request):
    queryset = Incidencia.objects.all()
    estado = request.GET.get('estado')
    prioridad = request.GET.get('prioridad')
    if estado:
        queryset = queryset.filter(estado=estado)
    if prioridad:
        queryset = queryset.filter(prioridad=prioridad)
    return render(request, 'incidencias/lista.html', {
        'incidencias': queryset,
        'estado_filtro': estado,
        'prioridad_filtro': prioridad,
    })


@login_required
def crear_incidencia(request):
    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Incidencia creada correctamente")
            return redirect('lista_incidencias')
    else:
        form = IncidenciaForm()
    return render(request, 'incidencias/form.html', {'form': form, 'titulo': 'Nueva Incidencia'})


@login_required
def detalle_incidencia(request, pk):
    incidencia = get_object_or_404(Incidencia, pk=pk)
    return render(request, 'incidencias/detalle.html', {'incidencia': incidencia})


@login_required
def editar_incidencia(request, pk):
    incidencia = get_object_or_404(Incidencia, pk=pk)
    if request.method == 'POST':
        form = IncidenciaForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            messages.success(request, "Incidencia actualizada")
            return redirect('detalle_incidencia', pk=pk)
    else:
        form = IncidenciaForm(instance=incidencia)
    return render(request, 'incidencias/form.html', {'form': form, 'titulo': 'Editar Incidencia'})


@login_required
def eliminar_incidencia(request, pk):
    incidencia = get_object_or_404(Incidencia, pk=pk)
    if request.method == 'POST':
        incidencia.delete()
        messages.success(request, "Incidencia eliminada")
        return redirect('lista_incidencias')
    return render(request, 'incidencias/eliminar_confirm.html', {'incidencia': incidencia})
