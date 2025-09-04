import pytest
from faker import Faker
from api_tests.helpers.api_client import ApiClient

fake = Faker()

@pytest.fixture(scope="module")
def api_client():
    client = ApiClient()
    username = fake.user_name()
    password = "Password123!"
    client.create_user(username, password)
    client.generate_token()
    return client

def test_user_is_authorized(api_client):
    response = api_client.is_authorized()
    assert response.status_code == 200
    assert response.json() is True

def test_list_and_rent_books(api_client):
    response = api_client.list_books()
    assert response.status_code == 200
    books = response.json()["books"]
    assert len(books) > 0

    book_ids = [books[0]["isbn"], books[1]["isbn"]]
    rent = api_client.rent_books(book_ids)
    assert rent.status_code in [200, 201]

def test_user_details(api_client):
    response = api_client.get_user_details()
    assert response.status_code == 200
    data = response.json()
    assert "books" in data
    assert len(data["books"]) >= 2
