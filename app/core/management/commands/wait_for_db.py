# Beacuse of this directory structure Django will automatically
# detech this command when using python manange.py
"""
Django Command to wait for database to be available
"""

import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
# error django throws when database is not ready
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for a database"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write((self.style.SUCCESS('Database available!')))
