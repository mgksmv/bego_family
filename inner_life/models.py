import sys
from PIL import Image as PILImage
from io import BytesIO

from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from ckeditor_uploader.fields import RichTextUploadingField

from accounts.models import Position
from departments.models import Employee
from config.validators import validate_video


def save_gallery(instance, filename):
    try:
        return 'inner_life/gallery/' + '/'.join([instance.name, filename])
    except AttributeError:
        return 'inner_life/gallery/' + '/'.join([instance.parent_model.name, filename])


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


class Image(models.Model):
    parent_model = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')
    image = models.ImageField(upload_to=save_gallery, verbose_name='Фото')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Фото'
    
    def __str__(self):
        return self.description


class Video(models.Model):
    parent_model = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE, verbose_name='Родительская модель')
    video = models.FileField(upload_to=save_gallery, validators=[validate_video], verbose_name='Видео')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.description


# class BestEmployees(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
#     name = models.CharField(max_length=100, verbose_name='Название')
#     slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
