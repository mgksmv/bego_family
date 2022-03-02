from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from accounts.models import Position
from config.validators import validate_video, validate_pdf


def save(instance, filename):
    return 'regulations/' + '/'.join([instance.parent_model.name, filename])


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

class Reglament(Base):
    class Meta:
        verbose_name = 'регламент/правило'
        verbose_name_plural = 'Общие правила и регламенты'


class Penalty(Base):
    class Meta:
        verbose_name = 'штрафная сетка'
        verbose_name_plural = 'Штрафная сетка'


class Bonus(Base):
    class Meta:
        verbose_name = 'премиальная сетка'
        verbose_name_plural = 'Премиальная сетка'


# Inlines

class ImageReglament(BaseImage):
    parent_model = models.ForeignKey(Reglament, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class ImagePenalty(BaseImage):
    parent_model = models.ForeignKey(Penalty, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class ImageBonus(BaseImage):
    parent_model = models.ForeignKey(Bonus, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')


class VideoReglament(BaseVideo):
    parent_model = models.ForeignKey(Reglament, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoPenalty(BaseVideo):
    parent_model = models.ForeignKey(Penalty, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class VideoBonus(BaseVideo):
    parent_model = models.ForeignKey(Bonus, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')


class PDFReglament(BasePDF):
    parent_model = models.ForeignKey(Reglament, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFPenalty(BasePDF):
    parent_model = models.ForeignKey(Penalty, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')

class PDFBonus(BasePDF):
    parent_model = models.ForeignKey(Bonus, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')
