from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_cliente, name='clientes_crear'),
    path('editar/<int:cliente_id>/', views.editar_cliente, name='clientes_editar'),
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='clientes_eliminar'),
]