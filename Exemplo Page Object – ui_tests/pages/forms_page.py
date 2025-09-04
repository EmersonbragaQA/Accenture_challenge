from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormsPage:
    URL = "https://demoqa.com/automation-practice-form"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def fill_form(self, first_name, last_name, email):
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)

    def submit(self):
        self.driver.find_element(By.ID, "submit").click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
        )
        return self.driver.find_element(By.ID, "example-modal-sizes-title-lg").is_displayed()
