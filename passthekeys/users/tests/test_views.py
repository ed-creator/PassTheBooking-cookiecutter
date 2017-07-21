from django.test import RequestFactory
from test_plus.test import TestCase
from django.test import Client
from unittest.mock import patch, MagicMock
from passthekeys.users.models import User



from ..views import (
    UserRedirectView,
    UserUpdateView
)

class BaseUserTestCase(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()


class TestUserRedirectView(BaseUserTestCase):

    def test_get_redirect_url(self):
        # Instantiate the view directly. Never do this outside a test!
        view = UserRedirectView()
        # Generate a fake request
        request = self.factory.get('/fake-url')
        # Attach the user to the request
        request.user = self.user
        # Attach the request to the view
        view.request = request
        # Expect: '/users/testuser/', as that is the default username for
        #   self.make_user()
        self.assertEqual(
            view.get_redirect_url(),
            '/users/testuser/'
        )


class TestUserUpdateView(BaseUserTestCase):

    c = Client()

    def setUp(self):
        # call BaseUserTestCase.setUp()
        super(TestUserUpdateView, self).setUp()
        # Instantiate the view directly. Never do this outside a test!
        self.view = UserUpdateView()
        # Generate a fake request
        request = self.factory.get('/fake-url')
        # Attach the user to the request
        request.user = self.user
        # Attach the request to the view
        self.view.request = request

    def test_get_success_url(self):
        # Expect: '/users/testuser/', as that is the default username for
        #   self.make_user()
        self.assertEqual(
            self.view.get_success_url(),
            '/users/testuser/'
        )

    def test_get_object(self):
        # Expect: self.user, as that is the request's user object
        self.assertEqual(
            self.view.get_object(),
            self.user
        )

    def test_user_login(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get('/users/testuser/')
        self.assertEqual(response.status_code, 200)

    def test_user_update_page(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get('/users/~update/')
        self.assertEqual(response.status_code, 200)

    def test_user_update_details(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get('/users/~update/')
        self.assertContains(response, "testuser")

    @patch('passthekeys.users.models.User.save', MagicMock(name="save"))
    def test_user_can_update_details(self):
        data = {'name':'Edward Wad',
                'phone_number':'+447813611455',
                'primary_city':'Bath'}
        request = self.factory.post('/users/~update/', data)
        request.user = self.user
        response = UserUpdateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.save.called)
        self.assertEqual(User.save.call_count, 0)
