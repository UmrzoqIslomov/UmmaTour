from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=36)
    short_description = models.TextField()
    slug = models.SlugField(max_length=128, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    ctg = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=64)
    tarif = models.CharField(max_length=128)
    date = models.CharField(max_length=64)
    muddati = models.CharField(max_length=128)
    menu = models.CharField(max_length=128)
    distance = models.CharField(max_length=24)


class Contact(models.Model):
    adress = models.CharField(max_length=128)
    ishvaqti = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    whatsup = models.CharField(max_length=128)


class CustomUserManager(BaseUserManager):
    """
    Custom category model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError('The Username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)


class AdminUser(AbstractUser):
    name = models.CharField(max_length=128)
    username = models.CharField(max_length=128, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=256)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
