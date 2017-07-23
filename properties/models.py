from django.db import models
from passthekeys.users.models import User

class Property(models.Model):
    """ holding information about property details,
        e.g. address, number of bedrooms, etc.
        A property must be connected to a client,
        and a client may have many properties."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_one = models.CharField(max_length=200,verbose_name= ('Address'))
    address = models.CharField(max_length=200, verbose_name= ('Post Code'))
    no_of_bedroom = models.IntegerField(default=0, verbose_name= ('Number of Bedrooms'))
    sq_feet = models.IntegerField(default=0, verbose_name= ('Square Feet'))

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.address_line_one
