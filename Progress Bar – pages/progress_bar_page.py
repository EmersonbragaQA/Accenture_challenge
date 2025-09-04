from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProgressBarPage:
    URL = "https://demoqa.com/progress-bar"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def start_and_stop_at(self, percent):
        self.driver.find_element(By.ID, "startStopButton").click()
        WebDriverWait(self.driver, 10).until(
            lambda d: int(d.find_element(By.CLASS_NAME, "progress-bar").get_attribute("aria-valuenow")) >= percent
        )
        self.driver.find_element(By.ID, "startStopButton").click()
        current_value = int(self.driver.find_element(By.CLASS_NAME, "progress-bar").get_attribute("aria-valuenow"))
        return current_value

    def run_to_100_and_reset(self):
        self.driver.find_element(By.ID, "startStopButton").click()
        WebDriverWait(self.driver, 15).until(
            lambda d: int(d.find_element(By.CLASS_NAME, "progress-bar").get_attribute("aria-valuenow")) == 100
        )
        self.driver.find_element(By.ID, "resetButton").click()
