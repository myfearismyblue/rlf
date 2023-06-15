from functools import partial

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .validators import UnicodeSpaceUsernameValidator



def _id_autofill(qualname):
    """
    An auxiliary func to increment ids by default.
    For example: id = models.IntegerField(primary_key=True, default=partial(_id_autofill, qualname=__qualname__))
    """
    last = globals()[qualname].objects.last()
    if not last:
        return 1
    else:
        return last.id + 1


class TeacherModel(models.Model):
    id = models.IntegerField(primary_key=True, default=partial(_id_autofill, qualname=__qualname__))
    first_name = models.CharField(max_length=64, null=False, blank=False)
    second_name = models.CharField(max_length=64, null=False, blank=False)

    # photo = models.ImageField()     # FIXME: consider URLField here

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class TopicModel(models.Model):
    id = models.IntegerField(primary_key=True, default=partial(_id_autofill, qualname=__qualname__))
    name = models.CharField(max_length=128, null=False, blank=False)

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')

    def __str__(self):
        return f'{self.name}'


class Topic_Module(models.Model):
    id = models.IntegerField(primary_key=True, default=partial(_id_autofill, qualname=__qualname__))
    topic = models.ForeignKey(TopicModel, on_delete=models.CASCADE, related_name='modules')
    module = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = _('Module')
        verbose_name_plural = _('Modules')

    def __str__(self):
        if not self.module:
            return f'{self.topic}'
        return f'{self.topic} - {self.module}'



class EventModel(models.Model):
    id = models.IntegerField(primary_key=True, default=partial(_id_autofill, qualname=__qualname__))
    start_date = models.DateField()
    end_date = models.DateField()
    country = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey('cities_light.City', on_delete=models.SET_NULL, null=True, blank=True)
    teachers = models.ManyToManyField(TeacherModel, related_name='events', blank=True)
    topic_modules = models.ManyToManyField(Topic_Module)

    def get_superuser_url(self):
        url = f'/admin{self._meta.app_label}/{self._meta.model_name}/'
        return url

    def get_su_item_change(self):
        url = f'/admin{self._meta.app_label}/{self._meta.model_name}/{self.id}/change/'
        return url

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return f'{self.city.name}. {self.start_date.strftime("%d %B %Y")} - {self.end_date.strftime("%d %B %Y")}.'


class RegionalAssociationModel(models.Model):
    id = models.IntegerField(primary_key=True, default=partial(_id_autofill, qualname=__qualname__))
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    address = models.CharField(max_length=512, blank=False, null=False)
    person = models.CharField(max_length=256, blank=True, null=True)
    telephone = models.CharField(max_length=16, blank=True, null=False, default='')
    web_site = models.CharField(max_length=128, blank=True, null=False, default='')
    e_mail = models.EmailField(blank=True, null=True)

    def get_absolute_url(self):
        return ''.join((reverse('associations'), '/id', str(self.id)))

    def get_superuser_url(self):
        url = f'/admin{self._meta.app_label}/{self._meta.model_name}/'
        return url

    def get_su_item_change(self):
        url = f'/admin{self._meta.app_label}/{self._meta.model_name}/{self.id}/change/'
        return url

    class Meta:
        verbose_name = _('Regional Association')
        verbose_name_plural = _('Regional Associations')

    def __str__(self):
        return f'{self.name}'


class RolfUser(AbstractUser):
    username_validator = UnicodeSpaceUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits, @/./+/-/_  and space only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_("email address"), blank=True, unique=True)
    REQUIRED_FIELDS = ['email']

    confirmation_key = models.CharField(max_length=64)
    confirmation_key_time = models.DateTimeField(_("Token created at"), null=True)

    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    def get_redis_confirmation_key_name(self):
        return ''.join((str(self.id), '_confirmation_key', ))


class UserProfile(models.Model):
    user = models.OneToOneField(RolfUser, on_delete=models.CASCADE, primary_key=True, related_name='profile')


@receiver(post_save, sender=RolfUser)
def create_favorites(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)