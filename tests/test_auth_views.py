""" Test auth views. """


import unittest
import features


class AuthRegisterTest(unittest.TestCase):
    """
    Test the auth.register view.
    """

    def setUp(self):
        app = features.create_app()
        self.client = app.test_client()

    def test_register_new_user(self):
        self.assertEqual(self.client.get('auth/register').status, '200 OK')
        response = self.client.get('auth/register')


# test auth.login view
def test_login(client):
    response = client.get('auth/login')
    assert response.status == '200 OK'
    html = response.get_data(as_text=True)
    assert '<title>IWS Feature Requests - Login</title>' in html




