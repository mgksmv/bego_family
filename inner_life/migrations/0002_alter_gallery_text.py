# Generated by Django 4.0.2 on 2022-03-01 17:44

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inner_life', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание'),
        ),
    ]