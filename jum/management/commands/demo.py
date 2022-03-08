from django.core.management import BaseCommand

from jum.models import Specialty, Vacancy, Company


class Command(BaseCommand):
    def handle(self, *args, **options):
        x = Specialty.objects.get(code='backend')
        print(x.id)
