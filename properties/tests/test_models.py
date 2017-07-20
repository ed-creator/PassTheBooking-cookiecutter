from test_plus.test import TestCase
from unittest import mock

from properties.models import Property
from passthekeys.users.models import User

class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()

        Property.objects.create(owner=self.user,
                    address_line_one = "Flat 1, High Street",
                    address = "E2 6JD",
                    no_of_bedroom = 2,
                    sq_feet = 100,
                    pk = 1
                    )

    def test__str__(self):
        """Calling Property returns string"""
        house_1 = Property.objects.get(pk=1)
        self.assertEqual(house_1.__str__(), 'Flat 1, High Street')
