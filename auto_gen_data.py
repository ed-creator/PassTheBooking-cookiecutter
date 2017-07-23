from passthekeys.users.models import User
from properties.models import Property
from bookings.models import Booking

class AutoGenerateData():

    names = ['Alice','Ben','Chloe','Donald']

    def gen_data(names):
        for index, e in enumerate(names):
            user = User.objects.create(username = e + 'susername',
                                email = 'user@user' + str(index) + '.com',
                                password = 'thisismypassword',
                                name = e,
                                primary_city = 'Bath',
                                phone_number = '+447813611457'
                                )
            user.set_password('123')
            user.save()
            Property.objects.create(owner = User.objects.get(name = e),
                                address_line_one = 'no. ' + str(index) + ' test street',
                                address = 'EC' + str(index) + 'TST',
                                no_of_bedroom = index,
                                sq_feet = index * 100
                                )
            Booking.objects.create(booking_property = Property.objects.get(no_of_bedroom = index),
                                date_of_check_in = '2017-10-25',
                                date_of_check_out = '2017-10-29',
                                guest_name = "Dave Davidson"
                                )
        return User.objects.all(), Property.objects.all(), Booking.objects.all()
