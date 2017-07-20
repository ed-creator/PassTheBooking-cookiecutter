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

        self.user = self.make_user()

    def test_list_reverse(self):
        """users:list should reverse to /users/."""
        self.assertEqual(reverse('users:list'), '/users/')

    def test_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve('/users/').view_name, 'users:list')
