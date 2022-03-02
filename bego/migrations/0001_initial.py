# Generated by Django 4.0.2 on 2022-02-21 18:55

import bego.models
import ckeditor_uploader.fields
import config.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'история',
                'verbose_name_plural': 'История BEGO',
            },
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'миссия BEGO',
                'verbose_name_plural': 'Миссия BEGO',
            },
        ),
        migrations.CreateModel(
            name='OrgStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'орг. структура',
                'verbose_name_plural': 'Орг. структура',
            },
        ),
        migrations.CreateModel(
            name='VideoOrgStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=bego.models.save, validators=[config.validators.validate_video], verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bego.orgstructure', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoMission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=bego.models.save, validators=[config.validators.validate_video], verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bego.mission', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=bego.models.save, validators=[config.validators.validate_video], verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bego.history', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PDFOrgStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=bego.models.save, validators=[config.validators.validate_pdf], verbose_name='PDF файл')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bego.orgstructure', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'pdf',
                'verbose_name_plural': 'PDF',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PDFMission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=bego.models.save, validators=[config.validators.validate_pdf], verbose_name='PDF файл')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bego.mission', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'pdf',
                'verbose_name_plural': 'PDF',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PDFHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=bego.models.save, validators=[config.validators.validate_pdf], verbose_name='PDF файл')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bego.history', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'pdf',
                'verbose_name_plural': 'PDF',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageOrgStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=bego.models.save, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bego.orgstructure', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageMission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=bego.models.save, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bego.mission', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=bego.models.save, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bego.history', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
                'abstract': False,
            },
        ),
    ]
