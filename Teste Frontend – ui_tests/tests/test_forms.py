from faker import Faker
from ui_tests.pages.forms_page import FormsPage

fake = Faker()

def test_submit_form(browser):
    page = FormsPage(browser)
    page.load()
    page.fill_form(fake.first_name(), fake.last_name(), fake.email())
    popup_displayed = page.submit()
    assert popup_displayed is True
