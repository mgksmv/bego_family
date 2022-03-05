# Generated by Django 4.0.2 on 2022-03-04 18:48

import ckeditor_uploader.fields
import config.validators
from django.db import migrations, models
import django.db.models.deletion
import inner_life.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('departments', '0004_alter_department_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to=inner_life.models.save_gallery, verbose_name='Превью фото')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
        migrations.CreateModel(
            name='Giveaway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('img', models.ImageField(blank=True, default='default-traineeship.png', upload_to=inner_life.models.save_others, verbose_name='Фото')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'конкурс',
                'verbose_name_plural': 'Конкурсы',
            },
        ),
        migrations.CreateModel(
            name='Nomination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('img', models.ImageField(blank=True, default='default-traineeship.png', upload_to=inner_life.models.save_others, verbose_name='Фото')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'наминация',
                'verbose_name_plural': 'Наминации',
            },
        ),
        migrations.CreateModel(
            name='RecordBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('img', models.ImageField(blank=True, default='default-traineeship.png', upload_to=inner_life.models.save_others, verbose_name='Фото')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'книга рекордов',
                'verbose_name_plural': 'Книга рекордов',
            },
        ),
        migrations.CreateModel(
            name='Tradition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('img', models.ImageField(blank=True, default='default-traineeship.png', upload_to=inner_life.models.save_others, verbose_name='Фото')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'традиция',
                'verbose_name_plural': 'Традиция',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('img', models.ImageField(blank=True, default='default-traineeship.png', upload_to=inner_life.models.save_others, verbose_name='Фото')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='VideoVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=inner_life.models.save_others, validators=[config.validators.validate_video], verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.video', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoTradition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=inner_life.models.save_others, validators=[config.validators.validate_video], verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.tradition', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoRecordBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=inner_life.models.save_others, validators=[config.validators.validate_video], verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.recordbook', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoNomination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=inner_life.models.save_others, validators=[config.validators.validate_video], verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.nomination', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoGiveaway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=inner_life.models.save_others, validators=[config.validators.validate_video], verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.giveaway', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PDFVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=inner_life.models.save_others, validators=[config.validators.validate_pdf], verbose_name='PDF файл')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.video', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'pdf',
                'verbose_name_plural': 'PDF',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PDFTradition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=inner_life.models.save_others, validators=[config.validators.validate_pdf], verbose_name='PDF файл')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.tradition', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'pdf',
                'verbose_name_plural': 'PDF',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PDFRecordBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=inner_life.models.save_others, validators=[config.validators.validate_pdf], verbose_name='PDF файл')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.recordbook', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'pdf',
                'verbose_name_plural': 'PDF',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PDFNomination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=inner_life.models.save_others, validators=[config.validators.validate_pdf], verbose_name='PDF файл')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.nomination', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'pdf',
                'verbose_name_plural': 'PDF',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PDFGiveaway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=inner_life.models.save_others, validators=[config.validators.validate_pdf], verbose_name='PDF файл')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.giveaway', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'pdf',
                'verbose_name_plural': 'PDF',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=inner_life.models.save_others, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.video', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageTradition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=inner_life.models.save_others, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.tradition', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageRecordBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=inner_life.models.save_others, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.recordbook', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageNomination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=inner_life.models.save_others, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.nomination', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageGiveaway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=inner_life.models.save_others, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.giveaway', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GalleryVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=inner_life.models.save_gallery, validators=[config.validators.validate_video], verbose_name='Видео')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.gallery', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=inner_life.models.save_gallery, verbose_name='Фото')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Описание')),
                ('parent_model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inner_life.gallery', verbose_name='Родительская модель')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.department', verbose_name='Подразделение')),
                ('participants', models.ManyToManyField(blank=True, to='departments.Employee', verbose_name='Участники')),
            ],
            options={
                'verbose_name': 'мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='BestEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('access', models.ManyToManyField(blank=True, to='accounts.Position', verbose_name='Уровень доступа')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'лучший сотрудник',
                'verbose_name_plural': 'Лучшие сотрудники',
            },
        ),
    ]
