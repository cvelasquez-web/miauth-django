from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        
        if username and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username, email, password)
                self.stdout.write(self.style.SUCCESS(f'Superusuario {username} creado con éxito.'))
            else:
                self.stdout.write(self.style.WARNING('El superusuario ya existe.'))