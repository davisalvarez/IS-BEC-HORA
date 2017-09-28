from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager

#from .managers import UserManager
from django.contrib.auth.models import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    carne = models.IntegerField(_('carne'))
    horasPendientes = models.IntegerField(_('H. Pendientes'))
    horasRealizadas = models.IntegerField(_('H. Realizadas'))
    admin = models.BooleanField(_('admin'), default=False)

    #nombre = models.CharField(max_length=64)
    #correo =  models.EmailField(max_length=64)
    username = models.CharField(max_length=16, unique=True)
    #contrasena = models.CharField(max_length=64, blank=True)
    # Campos por defecto
    email = models.EmailField(_('email address'), max_length=30, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',
                       'carne',
                       'horasPendientes',
                       'horasRealizadas',
                       'admin',
                    ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Actividad(models.Model):
    nombre = models.CharField(max_length=64, null=False)
    descripcion = models.CharField(max_length=255, null=False, default="Datos de la Actividad:")
    date = models.DateTimeField()
    horas = models.IntegerField()
    carne = models.IntegerField()

    class Meta:
        verbose_name = _('Actividad')
        verbose_name_plural = _('Actividades')

class AsigActividad(models.Model):
    idActividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, carne, horasPendientes, horasRealizadas, admin,password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(username=username, **extra_fields)
        user = self.model(horasPendientes=horasPendientes, **extra_fields)
        user = self.model(horasRealizadas=horasRealizadas, **extra_fields)
        user = self.model(admin=admin, **extra_fields)
        #newEmail= email+'@uvg.edu.gt'
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)