from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Vacía todas las tablas de la base de datos'

    def handle(self, *args, **options):
        self.stdout.write("Vaciando la base de datos...")
        # El comando 'flush' vacía los datos pero mantiene las tablas
        call_command('flush', '--noinput')
        self.stdout.write(self.style.SUCCESS('Base de datos vaciada correctamente.'))