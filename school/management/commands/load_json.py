from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import phones from school.json'

    def handle(self, *args, **options):
        from school.management.commands.migrate_json import start_migrate, migrate_many_to_many
        start_migrate()
        migrate_many_to_many()