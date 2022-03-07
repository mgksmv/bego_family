from faker import Faker

from django.core.management.base import BaseCommand
from departments.models import Traineeship, Department
from accounts.models import Position


class Command(BaseCommand):
    help = 'Заполняет случайными данными модель Traineeship.'

    def add_arguments(self, parser):
        parser.add_argument('quantity', action='append', type=int)
    
    def handle(self, *args, **options):
        fake = Faker('ru-ru')
        
        day = 0
        for _ in range(options['quantity'][0]):
            day += 1
            instance = Traineeship.objects.create(
                department=Department.objects.get(id=1),
                day=day,
                name=fake.first_name(),
                text=fake.paragraph(nb_sentences=5),
                slug=fake.lexify(text='??????????'),
            )
            for position in Position.objects.all():
                instance.access.add(position)
