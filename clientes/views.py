from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ClienteForm
from .models import Cliente


@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            messages.success(request, f'Cliente guardado: {cliente.nombre} ({cliente.correo})')
            return redirect('clientes_crear')
    else:
        form = ClienteForm()

    clientes = Cliente.objects.order_by('-id')
    return render(request, 'clientes/create.html', {
        'form': form,
        'clientes': clientes,
    })


@login_required
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cliente actualizado: {cliente.nombre}')
            return redirect('clientes_crear')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/editar.html', {
        'form': form,
        'cliente': cliente
    })


@login_required
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        nombre = cliente.nombre
        cliente.delete()
        messages.success(request, f'Cliente eliminado: {nombre}')
        return redirect('clientes_crear')
        
    return render(request, 'clientes/eliminar.html', {'cliente': cliente})