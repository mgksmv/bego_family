from faker import Faker

from django.core.management.base import BaseCommand
from inner_life.models import Event
from accounts.models import Position
from departments.models import Employee


class Command(BaseCommand):
    help = 'Заполняет случайными данными модель Event.'

    def add_arguments(self, parser):
        parser.add_argument('quantity', action='append', type=int)
    
    def handle(self, *args, **options):
        fake = Faker('ru-ru')
        
        for _ in range(options['quantity'][0]):
            instance = Event.objects.create(
                date=fake.date(),
                name=fake.name(),
                text=fake.paragraph(nb_sentences=5),\
                slug=fake.lexify(text='??????????'),
            )
            for position in Position.objects.all():
                instance.access.add(position)
            for employee in Employee.objects.all():
                instance.participants.add(employee)
