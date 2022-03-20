from django.core.management import BaseCommand

from jum.models import Vacancy


class Command(BaseCommand):
    def handle(self, *args, **options):
        x = 2
        print(
            Vacancy.objects.get(id=x).company
        )
