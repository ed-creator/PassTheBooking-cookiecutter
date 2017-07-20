from test_plus.test import TestCase

from properties.models import Property
from bookings.models import Booking

class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()
        prop_1 = Property.objects.create(owner=self.user,
                    address_line_one = "Flat 1, High Street",
                    address = "E2 6JD",
                    no_of_bedroom = 2,
                    sq_feet = 100
                    )
        Booking.objects.create(booking_property=prop_1,
                            date_of_check_in = '2017-10-25',
                            date_of_check_out = '2017-10-29',
                            guest_name = 'testguest'
                            )

    def test__str__(self):
        """Calling Booking returns the address and relevant dates"""
        booking_1 = Booking.objects.get(pk=1)
        self.assertEqual(booking_1.__str__(),
                        'Flat 1, High Street from 2017-10-24 to 2017-10-28'
                        )
