from django.test import Client
from django.urls import reverse

def test_hello_world_view():
    client = Client()
    response = client.get(reverse('hello_world'))
    assert response.status_code == 200
    assert b'Hello World Nick!' in response.content
    assert b'Welcome to my Django app with Material Dashboard!' in response.content