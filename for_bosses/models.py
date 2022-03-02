from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from accounts.models import Position
from accounts.models import Account


class Vacancy(models.Model):
    position = models.CharField(max_length=100, verbose_name='Должность')
    text = RichTextUploadingField(verbose_name='Описание')
    image = models.ImageField(default='default-vacancy-pic.png', upload_to='images/vacancy_pics', verbose_name='Фото')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'открытие вакансии'
        verbose_name_plural = 'Открытие вакансии'

    def __str__(self):
        return self.position

    def get_vacancy_url(self):
        return reverse('vacancies')


class Dismissal(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО увольняемого')
    account = models.ForeignKey(Account, on_delete=models.CASCADE,
                                blank=True, null=True, verbose_name='Аккаунт',
                                help_text='Выберите аккаунт увольняемого, если таковой имеется.')
    text = RichTextUploadingField(verbose_name='Описание / причины увольнения')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'подача на увольнение'
        verbose_name_plural = 'Подачи на увольнение'

    def __str__(self):
        return self.name


class Permissions(models.Model):
    permission = models.ManyToManyField(Position, blank=True, verbose_name='Кому разрешено', related_name='permissions_access')

    class Meta:
        verbose_name = 'разрешение на страницы руководителей'
        verbose_name_plural = 'Разрешение на страницы руководителей'

    def __str__(self):
        return 'Настройки'
