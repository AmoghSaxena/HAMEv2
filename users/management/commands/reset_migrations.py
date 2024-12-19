import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Resets migrations, SQLite database, and __pycache__ folders'

    def handle(self, *args, **options):
        self.stdout.write('Resetting migrations, database, and __pycache__ folders...')

        # Delete SQLite database
        db_path = settings.DATABASES['default']['NAME']
        if os.path.isfile(db_path):
            os.remove(db_path)
            self.stdout.write(f'Deleted SQLite database: {db_path}')

        # Walk through all directories in the project
        for root, dirs, files in os.walk(settings.BASE_DIR):
            # Delete migration files
            if 'migrations' in dirs:
                migrations_path = os.path.join(root, 'migrations')
                for filename in os.listdir(migrations_path):
                    if filename != '__init__.py':
                        file_path = os.path.join(migrations_path, filename)
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                self.stdout.write(f'Deleted migration files in: {migrations_path}')

            # Delete __pycache__ folders
            if '__pycache__' in dirs:
                pycache_path = os.path.join(root, '__pycache__')
                shutil.rmtree(pycache_path)
                self.stdout.write(f'Deleted __pycache__ folder: {pycache_path}')

        self.stdout.write(self.style.SUCCESS('Successfully reset migrations, database, and __pycache__ folders'))