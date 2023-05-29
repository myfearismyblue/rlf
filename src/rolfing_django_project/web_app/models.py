from typing import Optional

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _



class TeacherModel(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=64, null=False, blank=False)
    second_name = models.CharField(max_length=64, null=False, blank=False)
    # photo = models.ImageField()     # FIXME: consider URLField here

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class TopicModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, null=False, blank=False)

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')

    def __str__(self):
        return f'{self.name}'


class Topic_Module(models.Model):
    id = models.IntegerField(primary_key=True)
    topic = models.ForeignKey(TopicModel, on_delete=models.CASCADE, related_name='modules')
    module = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        if not self.module:
            return f'{self.topic}'
        return f'{self.topic} - {self.module}'



class EventModel(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    country = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey('cities_light.City', on_delete=models.SET_NULL, null=True, blank=True)
    teachers = models.ManyToManyField(TeacherModel, related_name='events', blank=False, null=False)
    topic_modules = models.ManyToManyField(Topic_Module)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return f'{self.city.name}. {self.start_date.strftime("%d %B %Y")} - {self.end_date.strftime("%d %B %Y")}.'


class RegionalAssociationModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    slug = models.SlugField(max_length=128, blank=True, null=True, unique=True, default=None)
    address = models.CharField(max_length=512, blank=False, null=False)
    person = models.CharField(max_length=256, blank=False, null=False)
    telephone = models.CharField(max_length=16, blank=True, null=False, default='')
    web_site = models.CharField(max_length=128, blank=True, null=False, default='')
    e_mail = models.EmailField()

    def get_absolute_url(self):
        return ''.join((reverse('associations'), '/', str(self.slug)))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Regional Association')
        verbose_name_plural = _('Regional Associations')

    def __str__(self):
        return f'{self.name}'

