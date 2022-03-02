from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from accounts.models import Position
from config.validators import validate_video, validate_pdf


def save(instance, filename):
    return 'bego/' + '/'.join([instance.parent_model.name, filename])


# Base templates

class Base(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    text = RichTextUploadingField(verbose_name='Описание')
    access = models.ManyToManyField(Position, blank=True, verbose_name='Уровень доступа')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


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


# Main models

class History(Base):
    class Meta:
        verbose_name = 'история'
        verbose_name_plural = 'История BEGO'


class Mission(Base):
    class Meta:
        verbose_name = 'миссия BEGO'
        verbose_name_plural = 'Миссия BEGO'


class OrgStructure(Base):
    class Meta:
        verbose_name = 'орг. структура'
        verbose_name_plural = 'Орг. структура'


# Inlines

class ImageHistory(BaseImage):
    parent_model = models.ForeignKey(History, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class ImageMission(BaseImage):
    parent_model = models.ForeignKey(Mission, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class ImageOrgStructure(BaseImage):
    parent_model = models.ForeignKey(OrgStructure, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')


class VideoHistory(BaseVideo):
    parent_model = models.ForeignKey(History, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoMission(BaseVideo):
    parent_model = models.ForeignKey(Mission, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoOrgStructure(BaseVideo):
    parent_model = models.ForeignKey(OrgStructure, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')


class PDFHistory(BasePDF):
    parent_model = models.ForeignKey(History, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFMission(BasePDF):
    parent_model = models.ForeignKey(Mission, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFOrgStructure(BasePDF):
    parent_model = models.ForeignKey(OrgStructure, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')
