from django.core.urlresolvers import reverse, resolve

from test_plus.test import TestCase
from properties.models import Property
from passthekeys.users.models import User


class TestPropertyURLs(TestCase):
    """Test URL patterns for users app."""

    def setUp(self):
        self.user = self.make_user()
        Property.objects.create(owner=self.user,
                    address_line_one = "Flat 1, High Street",
                    address = "E2 6JD",
                    no_of_bedroom = 2,
                    sq_feet = 100)

    def test_new_property_reverse(self):
        """users:list should reverse to /users/testuser/new_property."""
        self.assertEqual(reverse('users:property:create_property', kwargs={'username': 'testuser'}), '/users/testuser/new_property/')

    def test_property_detail_resolve(self):
        """/users/testuser/new_property should resolve to users:property:create_property."""
        self.assertEqual(resolve('/users/testuser/new_property/').view_name, 'users:property:new_property')

    def test_property_detail_resolve(self):
        """/users/testuser/property/1 should resolve to users:property:property_detail."""
        self.assertEqual(resolve('/users/testuser/property/1/').view_name, 'users:property:property_detail')

    def test_property_detail_reverse(self):
        """users:property:property_detail should reverse to /users/testuser/property/1."""
        self.assertEqual(reverse('users:property:property_detail', kwargs={'username': 'testuser', 'pk': 1}), '/users/testuser/property/1/')
