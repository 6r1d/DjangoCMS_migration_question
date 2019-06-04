# -*- coding: utf-8 -*-
"""New user model"""

from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    """New user class"""
    username = models.CharField(
        max_length=settings.MAX_USERNAME_LENGTH,
        unique=True
    )
    first_name = models.CharField('first name', max_length=254, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    email = models.EmailField(
        'email address', max_length=254, unique=True, null=True
    )
    is_staff = models.BooleanField(
        'staff status', default=False, help_text=(
            'Designates whether the user can log into this admin '
            'site.'
        )
    )
    is_active = models.BooleanField(
        'active', default=True, help_text=(
            'Designates whether this user should be treated as '
            'active. Unselect this instead of deleting accounts.'
        )
    )
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        """Identifies users by their username."""
        return self.username
