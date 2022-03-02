# Generated by Django 4.0.2 on 2022-02-21 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=200, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'должность',
                'verbose_name_plural': 'Должность',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Логин')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Email')),
                ('profile_pic', models.ImageField(default='default-profile-pic.jpg', upload_to='images/profile_pics', verbose_name='Фото профиля')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('level', models.IntegerField(default=1, verbose_name='Уровень')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='Последний вход')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Админ')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Статус персонала')),
                ('is_superadmin', models.BooleanField(default=False, verbose_name='Статус суперпользователя')),
                ('position', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.position', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'аккаунт',
                'verbose_name_plural': 'Аккаунты',
            },
        ),
    ]