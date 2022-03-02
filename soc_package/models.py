from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from accounts.models import Position
from config.validators import validate_video, validate_pdf


def save(instance, filename):
    return 'soc_package/' + '/'.join([instance.parent_model.name, filename])


class SocPackage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    text = RichTextUploadingField(verbose_name='Описание')
    access = models.ManyToManyField(Position, blank=True, verbose_name='Уровень доступа')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'соц. пакет'
        verbose_name_plural = 'Социальный пакет'

    def __str__(self):
        return self.name


class Image(models.Model):
    parent_model = models.ForeignKey(SocPackage, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')
    image = models.ImageField(upload_to=save, verbose_name='Фото')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Фото'
    
    def __str__(self):
        return self.description


class Video(models.Model):
    parent_model = models.ForeignKey(SocPackage, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')
    video = models.FileField(upload_to=save, validators=[validate_video], verbose_name='Видео')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.description


class PDF(models.Model):
    parent_model = models.ForeignKey(SocPackage, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')
    pdf = models.FileField(upload_to=save, validators=[validate_pdf], verbose_name='PDF файл')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'pdf'
        verbose_name_plural = 'PDF'

    def __str__(self):
        return self.description
