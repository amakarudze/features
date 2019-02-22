""" Test features views. """


# Test app home page rendering.
def test_home_view(client):
    response = client.get('/')
    assert response.status == '200 OK'
    html = response.get_data(as_text=True)
    assert '<title>IWS Feature Requests - Home</title>' in html

