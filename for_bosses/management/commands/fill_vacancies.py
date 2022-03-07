from faker import Faker

from django.core.management.base import BaseCommand
from for_bosses.models import Vacancy


class Command(BaseCommand):
    help = 'Заполняет случайными данными модель Vacancy.'

    def add_arguments(self, parser):
        parser.add_argument('quantity', action='append', type=int)
    
    def handle(self, *args, **options):
        fake = Faker('ru-ru')
        
        for _ in range(options['quantity'][0]):
            Vacancy.objects.create(
                position=fake.name(),
                text=fake.paragraph(nb_sentences=5),\
                slug=fake.lexify(text='??????????'),
            )
