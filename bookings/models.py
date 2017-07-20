from django.db import models
from properties.models import Property

class Booking(models.Model):

    booking_property = models.ForeignKey(Property)
    date_of_check_in = models.DateTimeField('check in date')
    date_of_check_out = models.DateTimeField('check out date')
    guest_name = models.CharField(max_length=200)

    def __str__(self):
        return self.booking_property.__str__() + " from " + self.get_date_string(self.date_of_check_in) + " to " + self.get_date_string(self.date_of_check_out)

    def get_date_string(self, date):
        parsed_date = date.date()
        return parsed_date.__str__()
