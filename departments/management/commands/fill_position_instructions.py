import random
from faker import Faker

from django.core.management.base import BaseCommand
from departments.models import DepartmentReglament, Department
from accounts.models import Position


class Command(BaseCommand):
    help = 'Заполняет случайными данными модель DepartmentReglament.'

    def add_arguments(self, parser):
        parser.add_argument('quantity', action='append', type=int)
    
    def handle(self, *args, **options):
        fake = Faker('ru-ru')
        
        for _ in range(options['quantity'][0]):
            type_choice = ['position_instruction', 'job_instruction']

            instance = DepartmentReglament.objects.create(
                department=Department.objects.get(id=1),
                instruction_type=random.choice(type_choice),
                name=fake.first_name(),
                text=fake.paragraph(nb_sentences=5),
                slug=fake.lexify(text='??????????'),
            )
            for position in Position.objects.all():
                instance.access.add(position)
