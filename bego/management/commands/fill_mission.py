from faker import Faker

from django.core.management.base import BaseCommand
from bego.models import Mission
from accounts.models import Position


class Command(BaseCommand):
    help = 'Заполняет случайными данными модель Mission.'

    def add_arguments(self, parser):
        parser.add_argument('quantity', action='append', type=int)
    
    def handle(self, *args, **options):
        fake = Faker('ru-ru')
        
        for _ in range(options['quantity'][0]):
            instance = Mission.objects.create(
                name=fake.name(),
                text=fake.paragraph(nb_sentences=5),
                slug=fake.lexify(text='??????????'),
            )
            for position in Position.objects.all():
                instance.access.add(position)
