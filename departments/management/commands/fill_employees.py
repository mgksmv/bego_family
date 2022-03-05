from faker import Faker

from django.core.management.base import BaseCommand
from departments.models import Employee, Department
from accounts.models import Position


class Command(BaseCommand):
    help = 'Заполняет случайными данными модель Employee.'

    def add_arguments(self, parser):
        parser.add_argument('quantity', action='append', type=int)
    
    def handle(self, *args, **options):
        fake = Faker('ru-ru')
        
        for _ in range(options['quantity'][0]):
            instance = Employee.objects.create(
                department=Department.objects.get(id=1),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                bio=fake.paragraph(nb_sentences=5),
                birth_date=fake.date(),
                slug=fake.lexify(text='??????????'),
            )
