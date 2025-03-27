from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
   
    email = models.EmailField(_('email address'), unique=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', 
        null=True, 
        blank=True
    )
    bio = models.TextField(
        max_length=500, 
        blank=True, 
        null=True
    )
    date_of_birth = models.DateField(
        null=True, 
        blank=True
    )
    is_active_member = models.BooleanField(
        default=True, 
        help_text=_('Designates whether this user is an active member of the organization')
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')