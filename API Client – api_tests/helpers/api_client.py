import requests

BASE_URL = "https://demoqa.com"

class ApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.token = None
        self.user_id = None
        self.username = None
        self.password = None

    def create_user(self, username, password):
        url = f"{BASE_URL}/Account/v1/User"
        payload = {"userName": username, "password": password}
        response = self.session.post(url, json=payload)
        if response.status_code == 201:
            self.user_id = response.json()["userID"]
            self.username = username
            self.password = password
        return response

    def generate_token(self):
        url = f"{BASE_URL}/Account/v1/GenerateToken"
        payload = {"userName": self.username, "password": self.password}
        response = self.session.post(url, json=payload)
        if response.status_code == 200:
            self.token = response.json()["token"]
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})
        return response

    def is_authorized(self):
        url = f"{BASE_URL}/Account/v1/Authorized"
        payload = {"userName": self.username, "password": self.password}
        return self.session.post(url, json=payload)

    def list_books(self):
        url = f"{BASE_URL}/BookStore/v1/Books"
        return self.session.get(url)

    def rent_books(self, book_ids):
        url = f"{BASE_URL}/BookStore/v1/Books"
        payload = {"userId": self.user_id, "collectionOfIsbns": [{"isbn": b} for b in book_ids]}
        return self.session.post(url, json=payload)

    def get_user_details(self):
        url = f"{BASE_URL}/Account/v1/User/{self.user_id}"
        return self.session.get(url)
