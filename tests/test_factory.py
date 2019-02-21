""" Test application factory set up. """

from features import create_app


# Test create_app function for application factory set up.
def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


# Test hello function in create_app application factory.
def test_hello(client):
    response = client.get('/hello')
    assert b'Feature Requests App' in response.data
