""" Test auth views. """

def test_register(client):
    response = client.get('auth/register')
    assert response.status == '200 OK'
    html = response.get_data(as_text=True)
    assert '<title>IWS Feature Requests - Register</title>' in html

