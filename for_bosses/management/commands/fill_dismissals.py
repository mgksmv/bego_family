from faker import Faker

from django.core.management.base import BaseCommand
from for_bosses.models import Dismissal
from accounts.models import Account


class Command(BaseCommand):
    help = 'Заполняет случайными данными модель Dismissal.'

    def add_arguments(self, parser):
        parser.add_argument('quantity', action='append', type=int)
    
    def handle(self, *args, **options):
        fake = Faker('ru-ru')
        
        for _ in range(options['quantity'][0]):
            instance = Dismissal.objects.create(
                name=fake.name(),
                text=fake.paragraph(nb_sentences=5),
                account=Account.objects.get(id=1),
                slug=fake.lexify(text='??????????'),
            )
