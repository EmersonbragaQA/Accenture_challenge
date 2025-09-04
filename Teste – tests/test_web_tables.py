from faker import Faker
from ui_tests.pages.web_tables_page import WebTablesPage

fake = Faker()

def test_web_tables(browser):
    page = WebTablesPage(browser)
    page.load()

    page.add_record(fake.first_name(), fake.last_name(), fake.email(), 30, 5000, "QA")
    page.edit_record(4, 8000)
    page.delete_record(4)
