from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.conf import settings
from .utils import edit_avatar


class ClientManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        client = Client(email=email, **extra_fields)
        client.password = make_password(password)
        client.save()
        return client

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields['avatar'].name= email.replace('.', '-')+extra_fields['avatar'].name[-4:]
        client= self._create_user(email, password, **extra_fields)
        self.edit_picture(client)
        return client

    def edit_picture(self, client, editor=edit_avatar):
        edited=editor(client.avatar.path)
        return editor


    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        assert extra_fields['is_staff']
        assert extra_fields['is_superuser']
        return self._create_user(email, password, **extra_fields)


SEXES = (('m', 'M'), ('f', 'F'))


# User

class Client(AbstractUser):
    avatar = models.ImageField(upload_to=settings.MEDIA['AVATARS'])
    sex = models.CharField(max_length=1, choices=SEXES)  # m- male, f- female
    name = models.TextField()
    surname = models.TextField()
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = ClientManager()

    def __str__(self):
        if not self.is_staff:
            return str(self.name) + ' ' + str(self.surname)
        else:
            return self.email
    class Meta(AbstractUser.Meta):
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
# Create your models here.
