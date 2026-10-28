# Estas son las rutas de la aplicacion
"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from django.contrib import admin 

from django.contrib.auth import views as auth_views 

from django.urls import path, include
from django.urls import path 

from. import views 

from. forms import LoginForm 
 
from. import views

urlpatterns = [ 

   path('admin/', admin.site.urls), 

   path('', views.home, name='home'), 

   path('registro/', views.registro, name='registro'), 
    
   path('login/', auth_views.LoginView.as_view( 

       template_name='registration/login.html', 

       authentication_form=LoginForm, 

   ), name='login'), 

   path('logout/', auth_views.LogoutView.as_view(), name='logout'), 

   path('recuperar/', auth_views.PasswordResetView.as_view( 

       template_name='registration/password_reset_form.html', 

   ), name='password_reset'), 

   path('recuperar/enviado/', auth_views.PasswordResetDoneView.as_view( 

       template_name='registration/password_reset_done.html', 

   ), name='password_reset_done'), 

   path('recuperar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view( 

       template_name='registration/password_reset_confirm.html', 

   ), name='password_reset_confirm'), 

   path('recuperar/listo/', auth_views.PasswordResetCompleteView.as_view( 

       template_name='registration/password_reset_complete.html', 

   ), name='password_reset_complete'), 
   path('clientes/', include('clientes.urls')),  # Agrega esta línea para incluir las URLs de la aplicación "clientes"
]