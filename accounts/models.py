from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Position(models.Model):
    position_name = models.CharField(max_length=200, verbose_name='Должность')

    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'Должность'

    def __str__(self):
        return self.position_name


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('Пожалуйста, введите Email')

        if not username:
            raise ValueError('Пожалуйта, введите логин')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    username = models.CharField(max_length=100, unique=True, verbose_name='Логин')
    email = models.EmailField(max_length=100, blank=True, verbose_name='Email')
    position = models.ForeignKey(Position, default=None, null=True, on_delete=models.CASCADE, verbose_name='Должность')
    profile_pic = models.ImageField(default='default-profile-pic.jpg', upload_to='images/profile_pics', verbose_name='Фото профиля')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    level = models.IntegerField(default=1, verbose_name='Уровень')

    # required
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    last_login = models.DateTimeField(auto_now_add=True, verbose_name='Последний вход')
    is_active = models.BooleanField(default=False, verbose_name='Активный')
    is_admin = models.BooleanField(default=False, verbose_name='Админ')
    is_staff = models.BooleanField(default=False, verbose_name='Статус персонала')
    is_superadmin = models.BooleanField(default=False, verbose_name='Статус суперпользователя')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = MyAccountManager()

    class Meta:
        verbose_name = 'аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
