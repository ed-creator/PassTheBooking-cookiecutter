from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    CITY_CHOICES = (
    ('BA','Bath'),
    ('BN','Brighton'),
    ('BS','Bristol'),
    ('CB','Cambridge'),
    ('EH','Edinburgh'),
    ('L', 'London'),
    ('M', 'Manchester'),
    ('OX', 'Oxford'),
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    phone_number = PhoneNumberField(blank=True)
    primary_city = models.CharField(max_length=20,choices=CITY_CHOICES,blank=True)


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
