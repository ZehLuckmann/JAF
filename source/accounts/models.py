
from django.contrib.auth.models import User
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.apps import apps

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    furb_id = models.CharField(max_length=10,blank=True)
    rg = models.CharField(max_length=10,blank=True)
    cpf = models.CharField(max_length=10,blank=True)

    is_teacher = models.BooleanField(blank=True, null=True, default=False)
    is_federated = models.BooleanField(blank=True, null=True, default=False)
    is_graduated = models.BooleanField(blank=True, null=True, default=False)

    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)

    athletic = models.ForeignKey('athletic.Athletic', on_delete=models.DO_NOTHING,blank=True, null=True)

    is_active = models.BooleanField(_('active'), default=True)
    
    is_member = models.BooleanField('Membro', default=False)
    is_board = models.BooleanField('Diretoria', default=False)
    is_admin = models.BooleanField('Admin', default=False)

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)

    email = models.EmailField(blank=True)
    
   