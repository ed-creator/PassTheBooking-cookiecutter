from django.db import models
from passthekeys.users.models import User
# Create your models here.
class Property(models.Model):
    """ holding information about property details,
        e.g. address, number of bedrooms, etc.
        A property must be connected to a client,
        and a client may have many properties."""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_one = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    no_of_bedroom = models.IntegerField(default=0)
    sq_feet = models.IntegerField(default=0)

    def __str__(self):
        return self.address_line_one
