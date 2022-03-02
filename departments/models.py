from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from accounts.models import Position
from config.validators import validate_video, validate_pdf, validate_file


def save(instance, filename):
    try:
        return 'departments/' + '/'.join([instance.department.name, filename])
    except AttributeError:
        return 'departments/' + '/'.join([instance.parent_model.name, filename])


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    positioning = RichTextUploadingField(blank=True, verbose_name='Позиционирование')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'подразделение'
        verbose_name_plural = '       Подразделения'

    def __str__(self):
        return self.name


class Presentation(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Подразделение', related_name='presentations')
    name = models.CharField(max_length=100, verbose_name='Название')
    file = models.FileField(upload_to=save, validators=[validate_file], verbose_name='PDF файл')

    class Meta:
        verbose_name = 'презентация'
        verbose_name_plural = '     Презентация'
    
    def __str__(self):
        return self.name


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Подразделение', related_name='employees')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
    bio = RichTextUploadingField(blank=True, verbose_name='Биография')
    position = models.ForeignKey(Position, default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Должность')
    image = models.ImageField(default='default-profile-pic.jpg', upload_to=save, verbose_name='Фото')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = '      Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        if self.middle_name:
            return f'{self.first_name} {self.last_name} {self.middle_name}'
        return f'{self.first_name} {self.last_name}'


class DepartmentReglament(models.Model):
    TYPE_CHOICE = (
        ('position_instruction', 'Должностная инструкция'),
        ('job_instruction', 'Инструкция по работе'),
    )

    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Подразделение')
    instruction_type = models.CharField(max_length=255, default='position_instruction', choices=TYPE_CHOICE, verbose_name='Тип')
    name = models.CharField(max_length=100, verbose_name='Название')
    text = RichTextUploadingField(verbose_name='Описание')
    access = models.ManyToManyField(Position, blank=True, verbose_name='Уровень доступа', related_name='reglament_access')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'регламент'
        verbose_name_plural = '    Регламенты'

    def __str__(self):
        return self.name

    def get_position_url(self):
        return reverse('position_instructions', kwargs={'department': self.department.slug})
    
    def get_job_url(self):
        return reverse('job_instructions', kwargs={'department': self.department.slug})


class Traineeship(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Подразделение')
    name = models.CharField(max_length=100, verbose_name='Название')
    day = models.PositiveIntegerField(blank=True, null=True, verbose_name='День')
    img = models.ImageField(default='default-traineeship.png', upload_to=save, blank=True,
                              verbose_name='Фото урока')
    text = RichTextUploadingField(verbose_name='Описание')
    access = models.ManyToManyField(Position, blank=True, verbose_name='Уровень доступа', related_name='traineeship_access')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    prev_url = models.ForeignKey('self', null=True, default=None, blank=True, on_delete=models.CASCADE,
                                 verbose_name='Предыдущий урок', related_name='prev')
    next_url = models.ForeignKey('self', null=True, default=None, blank=True, on_delete=models.CASCADE,
                                 verbose_name='Следующий урок', related_name='next')

    class Meta:
        verbose_name = 'стажировка'
        verbose_name_plural = '   Стажировка'

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('traineeship', kwargs={'department': self.department.slug})
    

class Training(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Подразделение')
    name = models.CharField(max_length=100, verbose_name='Название')
    img = models.ImageField(default='default-traineeship.png', upload_to=save, blank=True,
                              verbose_name='Фото')
    text = RichTextUploadingField(verbose_name='Описание')
    access = models.ManyToManyField(Position, blank=True, verbose_name='Уровень доступа')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'обучение'
        verbose_name_plural = ' Обучение'

    def __str__(self):
        return self.name


class LevelUp(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Подразделение')
    name = models.CharField(max_length=100, verbose_name='Название')
    img = models.ImageField(default='default-traineeship.png', upload_to=save, blank=True,
                              verbose_name='Фото')
    text = RichTextUploadingField(verbose_name='Описание')
    access = models.ManyToManyField(Position, blank=True, verbose_name='Уровень доступа')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'повышение квалификации'
        verbose_name_plural = 'Повышение квалификации'

    def __str__(self):
        return self.name


# Base templates

class BaseImage(models.Model):
    image = models.ImageField(upload_to=save, verbose_name='Фото')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        abstract = True
        verbose_name = 'фото'
        verbose_name_plural = 'Фото'
    
    def __str__(self):
        return self.description


class BaseVideo(models.Model):
    video = models.FileField(upload_to=save, validators=[validate_video], verbose_name='Видео')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        abstract = True
        verbose_name = 'видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.description


class BasePDF(models.Model):
    pdf = models.FileField(upload_to=save, validators=[validate_pdf], verbose_name='PDF файл')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        abstract = True
        verbose_name = 'pdf'
        verbose_name_plural = 'PDF'

    def __str__(self):
        return self.description


# Inline models

class ImageDepartmentReglament(BaseImage):
    parent_model = models.ForeignKey(DepartmentReglament, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoDepartmentReglament(BaseVideo):
    parent_model = models.ForeignKey(DepartmentReglament, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFDepartmentReglament(BasePDF):
    parent_model = models.ForeignKey(DepartmentReglament, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')


class ImageTraineeship(BaseImage):
    parent_model = models.ForeignKey(Traineeship, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoTraineeship(BaseVideo):
    parent_model = models.ForeignKey(Traineeship, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFTraineeship(BasePDF):
    parent_model = models.ForeignKey(Traineeship, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')


class ImageTraining(BaseImage):
    parent_model = models.ForeignKey(Training, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoTraining(BaseVideo):
    parent_model = models.ForeignKey(Training, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFTraining(BasePDF):
    parent_model = models.ForeignKey(Training, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')


class ImageLevelUp(BaseImage):
    parent_model = models.ForeignKey(LevelUp, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoLevelUp(BaseVideo):
    parent_model = models.ForeignKey(LevelUp, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFLevelUp(BasePDF):
    parent_model = models.ForeignKey(LevelUp, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')
