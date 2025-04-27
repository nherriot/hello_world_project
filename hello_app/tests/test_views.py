from django.test import Client
from django.urls import reverse

def test_hello_world_view():
    client = Client()
    response = client.get(reverse('hello_world'))
    assert response.status_code == 200
    assert b'Hello World Nick!XXXXXX' in response.content
    assert b'Welcome to my Django app with Material Dashboard!' in response.content

def test_click_me_button():
    client = Client()
    response = client.get(reverse('hello_world'))
    assert response.status_code == 200
    # Check for button with correct class and onclick attribute
    assert b'<button class="btn btn-primary" onclick="alert(\'Button clicked!\')">' in response.content
    assert b'Click Me' in response.content