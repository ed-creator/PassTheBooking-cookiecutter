from test_plus.test import TestCase
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from unittest.mock import patch, MagicMock
from passthekeys.users.models import User
from properties.models import Property
from bookings.models import Booking
from django.core.urlresolvers import reverse

from ..views import BookingDetailView



class BaseBookingTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = self.make_user()

    def test_details(self):
        """Test that user can see their own property details when logged in"""
        test_prop = Property.objects.create(owner=self.user,
                            address_line_one = "Flat 1, High Street",
                            address = "E2 6JD",
                            no_of_bedroom = 2,
                            sq_feet = 100
                            )
        test_book = Booking.objects.create(booking_property=test_prop,
                            date_of_check_in = '2017-10-25',
                            date_of_check_out = '2017-10-29',
                            guest_name = 'testguest',
                            )
        test_pk = test_book.pk
        request = self.factory.get('/bookings/1/')
        request.user = self.user
        response = BookingDetailView.as_view()(request, pk=test_pk)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testguest")
        self.assertContains(response, "Check In: Oct. 25, 2017")
        self.assertContains(response, "Check Out: Oct. 29, 2017")
