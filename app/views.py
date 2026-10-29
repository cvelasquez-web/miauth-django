# Importaciones necesarias
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
    else:
        form = RegistroForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

# NUEVA VISTA: Recibe la señal de JavaScript para cerrar la sesión
def logout_forzado(request):
    logout(request)
    return HttpResponse(status=200)