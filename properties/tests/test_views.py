from test_plus.test import TestCase
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from unittest.mock import patch, MagicMock
from passthekeys.users.models import User
from properties.models import Property
from django.core.urlresolvers import reverse

from ..views import (
    PropertyDetailView,
    PropertyListView,
    PropertyUpdateView,
    PropertyCreateView
)

def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request

def add_middleware_to_response(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    return request

class BasePropertyTestCase(TestCase):

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
        test_pk = test_prop.pk
        request = self.factory.get('/user/testuser/property/1/')
        request.user = self.user
        response = PropertyDetailView.as_view()(request, pk=test_pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Flat 1, High Street")
        self.assertContains(response, "E2 6JD")

    def test_details_user_logged_out(self):
        """Test that user can't see others property details when logged out"""
        test_prop = Property.objects.create(owner=self.user,
        address_line_one = "Flat 1, High Street",
        address = "E2 6JD",
        no_of_bedroom = 2,
        sq_feet = 100
        )
        test_pk = test_prop.pk
        request = self.factory.get('/user/testuser/property/1/')
        request.user = AnonymousUser()
        response = PropertyDetailView.as_view()(request, pk=test_pk)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "E2 6JD")
        self.assertContains(response, "log in to view your property")

    @patch('properties.models.Property.save', MagicMock(name="save"))
    def test_createview(self):
        """Test to check a Property is saved when posting valid data to a CreateView"""
        data = {'address':'test address',
                'address_line_one':'test address line one',
                'no_of_bedroom':'3',
                'sq_feet':'300'
                }
        request = self.factory.post('/user/testuser/new_property/', data)
        request.user = self.user
        response = PropertyCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Property.save.called)
        self.assertEqual(Property.save.call_count, 1)

    @patch('properties.models.Property.save', MagicMock(name="save"))
    def test_createview(self):
        """Test to check a Property is saved when posting valid data to a CreateView"""
        data = {'address':'test address',
                'address_line_one':'test address line one',
                'no_of_bedroom':'3',
                }
        request = self.factory.post('/user/testuser/new_property/', data)
        request.user = AnonymousUser()
        response = PropertyCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Property.save.called)
        self.assertEqual(Property.save.call_count, 0)
