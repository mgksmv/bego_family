# Generated by Django 4.0.2 on 2022-02-21 18:55

import ckeditor_uploader.fields
import config.validators
from django.db import migrations, models
import django.db.models.deletion
import regulations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'премиальная сетка',
                'verbose_name_plural': 'Премиальная сетка',
            },
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'штрафная сетка',
                'verbose_name_plural': 'Штрафная сетка',
            },
        ),
        migrations.CreateModel(
            name='Reglament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'регламент/правило',
                'verbose_name_plural': 'Общие правила и регламенты',
            },
        ),
        migrations.CreateModel(
            name='VideoReglament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=regulations.models.save, validators=[config.validators.validate_video], verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='regulations.reglament', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoPenalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=regulations.models.save, validators=[config.validators.validate_video], verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='regulations.penalty', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoBonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=regulations.models.save, validators=[config.validators.validate_video], verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='regulations.bonus', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PDFReglament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=regulations.models.save, validators=[config.validators.validate_pdf], verbose_name='PDF файл')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='regulations.reglament', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'pdf',
                'verbose_name_plural': 'PDF',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PDFPenalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=regulations.models.save, validators=[config.validators.validate_pdf], verbose_name='PDF файл')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='regulations.penalty', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'pdf',
                'verbose_name_plural': 'PDF',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PDFBonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=regulations.models.save, validators=[config.validators.validate_pdf], verbose_name='PDF файл')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='regulations.bonus', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'pdf',
                'verbose_name_plural': 'PDF',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageReglament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=regulations.models.save, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='regulations.reglament', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImagePenalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=regulations.models.save, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='regulations.penalty', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageBonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=regulations.models.save, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='regulations.bonus', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
                'abstract': False,
            },
        ),
    ]
