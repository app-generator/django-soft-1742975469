# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    user_id = models.IntegerField(null=True, blank=True)
    user_purpose = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Farm(models.Model):

    #__Farm_FIELDS__
    farm_id = models.IntegerField(null=True, blank=True)
    activity = models.CharField(max_length=255, null=True, blank=True)
    farm_name = models.CharField(max_length=255, null=True, blank=True)
    farm_status = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Farm_FIELDS__END

    class Meta:
        verbose_name        = _("Farm")
        verbose_name_plural = _("Farm")


class Feeds(models.Model):

    #__Feeds_FIELDS__
    feed_type = models.CharField(max_length=255, null=True, blank=True)
    feed_store = models.CharField(max_length=255, null=True, blank=True)
    feed_quantity = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Feeds_FIELDS__END

    class Meta:
        verbose_name        = _("Feeds")
        verbose_name_plural = _("Feeds")


class Livestocks(models.Model):

    #__Livestocks_FIELDS__
    animal_quantity = models.IntegerField(null=True, blank=True)
    animal_purpose = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Livestocks_FIELDS__END

    class Meta:
        verbose_name        = _("Livestocks")
        verbose_name_plural = _("Livestocks")


class Employees(models.Model):

    #__Employees_FIELDS__
    department = models.CharField(max_length=255, null=True, blank=True)
    field_assigned = models.TextField(max_length=255, null=True, blank=True)
    national_id = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Employees_FIELDS__END

    class Meta:
        verbose_name        = _("Employees")
        verbose_name_plural = _("Employees")


class Machines(models.Model):

    #__Machines_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Machines_FIELDS__END

    class Meta:
        verbose_name        = _("Machines")
        verbose_name_plural = _("Machines")



#__MODELS__END
