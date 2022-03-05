import sys
from PIL import Image as PILImage
from io import BytesIO

from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from accounts.models import Position
from departments.models import Employee, Department
from config.validators import validate_video, validate_pdf


def save_gallery(instance, filename):
    try:
        return 'inner_life/gallery/' + '/'.join([instance.name, filename])
    except AttributeError:
        return 'inner_life/gallery/' + '/'.join([instance.parent_model.name, filename])


def save_others(instance, filename):
    try:
        return 'inner_life/other/' + '/'.join([instance.name, filename])
    except AttributeError:
        return 'inner_life/other/' + '/'.join([instance.parent_model.name, filename])


class Gallery(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    text = RichTextUploadingField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to=save_gallery, verbose_name='Превью фото')
    access = models.ManyToManyField(Position, blank=True, verbose_name='Уровень доступа')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'галерея'
        verbose_name_plural = 'Галерея'

    def save(self, **kwargs):
        output_size = (300, 300)
        output_thumb = BytesIO()

        img = PILImage.open(self.photo)
        img_name = self.photo.name.split('.')[0]

        if img.height > 300 or img.width > 300:
            img.thumbnail(output_size)
            img.save(output_thumb, format='JPEG', quality=90)

            self.photo = InMemoryUploadedFile(output_thumb, 'ImageField', f"{img_name}_thumb.jpg", 'image/jpeg', sys.getsizeof(output_thumb), None)

        super(Gallery, self).save()

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    parent_model = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')
    image = models.ImageField(upload_to=save_gallery, verbose_name='Фото')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Фото'
    
    def __str__(self):
        return self.description


class GalleryVideo(models.Model):
    parent_model = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')
    video = models.FileField(upload_to=save_gallery, validators=[validate_video], verbose_name='Видео')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.description


class BestEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    text = RichTextUploadingField(blank=True, verbose_name='Описание')
    access = models.ManyToManyField(Position, blank=True, verbose_name='Уровень доступа')

    class Meta:
        verbose_name = 'лучший сотрудник'
        verbose_name_plural = 'Лучшие сотрудники'

    def __str__(self):
        return self.employee.get_full_name()


class Event(models.Model):
    date = models.DateField(verbose_name='Дата')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Подразделение')
    name = models.CharField(max_length=100, verbose_name='Название')
    text = RichTextUploadingField(blank=True, verbose_name='Описание')
    participants = models.ManyToManyField(Employee, blank=True, verbose_name='Участники')
    access = models.ManyToManyField(Position, blank=True, verbose_name='Уровень доступа')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'мероприятие'
        verbose_name_plural = 'Мероприятия'

    @property
    def get_html_url(self):
        url = reverse('event_detail', args=(self.slug,))
        return f'<a href="{url}"> {self.name} </a>'
    
    def __str__(self):
        return self.name


class Base(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    img = models.ImageField(default='default-traineeship.png', upload_to=save_others, blank=True,
                              verbose_name='Фото')
    text = RichTextUploadingField(verbose_name='Описание')
    access = models.ManyToManyField(Position, blank=True, verbose_name='Уровень доступа')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        abstract = True

    def get_absolute_url(self):
        raise NotImplementedError

    def __str__(self):
        return self.name


#######################################################################################################
class RecordBook(Base):
    class Meta:
        verbose_name = 'книга рекордов'
        verbose_name_plural = 'Книга рекордов'
    
    def get_absolute_url(self):
        return reverse('record_book_detail', kwargs={'slug': self.slug})


class Video(Base):
    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'Видео'

    def get_absolute_url(self):
        return reverse('video_detail', kwargs={'slug': self.slug})


class Giveaway(Base):
    class Meta:
        verbose_name = 'конкурс'
        verbose_name_plural = 'Конкурсы'

    def get_absolute_url(self):
        return reverse('giveaways_detail', kwargs={'slug': self.slug})


class Tradition(Base):
    class Meta:
        verbose_name = 'традиция'
        verbose_name_plural = 'Традиция'

    def get_absolute_url(self):
        return reverse('traditions_detail', kwargs={'slug': self.slug})


class Nomination(Base):
    class Meta:
        verbose_name = 'наминация'
        verbose_name_plural = 'Наминации'

    def get_absolute_url(self):
        return reverse('nominations_detail', kwargs={'slug': self.slug})


# Base templates

class BaseImage(models.Model):
    image = models.ImageField(upload_to=save_others, verbose_name='Фото')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        abstract = True
        verbose_name = 'фото'
        verbose_name_plural = 'Фото'
    
    def __str__(self):
        return self.description


class BaseVideo(models.Model):
    video = models.FileField(upload_to=save_others, validators=[validate_video], verbose_name='Видео')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        abstract = True
        verbose_name = 'видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.description


class BasePDF(models.Model):
    pdf = models.FileField(upload_to=save_others, validators=[validate_pdf], verbose_name='PDF файл')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        abstract = True
        verbose_name = 'pdf'
        verbose_name_plural = 'PDF'

    def __str__(self):
        return self.description


# Inline models

class ImageRecordBook(BaseImage):
    parent_model = models.ForeignKey(RecordBook, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoRecordBook(BaseVideo):
    parent_model = models.ForeignKey(RecordBook, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFRecordBook(BasePDF):
    parent_model = models.ForeignKey(RecordBook, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')


class ImageVideo(BaseImage):
    parent_model = models.ForeignKey(Video, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoVideo(BaseVideo):
    parent_model = models.ForeignKey(Video, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFVideo(BasePDF):
    parent_model = models.ForeignKey(Video, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')


class ImageGiveaway(BaseImage):
    parent_model = models.ForeignKey(Giveaway, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoGiveaway(BaseVideo):
    parent_model = models.ForeignKey(Giveaway, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFGiveaway(BasePDF):
    parent_model = models.ForeignKey(Giveaway, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')


class ImageTradition(BaseImage):
    parent_model = models.ForeignKey(Tradition, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoTradition(BaseVideo):
    parent_model = models.ForeignKey(Tradition, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFTradition(BasePDF):
    parent_model = models.ForeignKey(Tradition, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')


class ImageNomination(BaseImage):
    parent_model = models.ForeignKey(Nomination, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoNomination(BaseVideo):
    parent_model = models.ForeignKey(Nomination, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFNomination(BasePDF):
    parent_model = models.ForeignKey(Nomination, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')
