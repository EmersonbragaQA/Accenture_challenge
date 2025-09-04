from selenium.webdriver.common.by import By

class BrowserWindowsPage:
    URL = "https://demoqa.com/browser-windows"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def open_new_window(self):
        self.driver.find_element(By.ID, "windowButton").click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        return self.driver.find_element(By.TAG_NAME, "h1").text
