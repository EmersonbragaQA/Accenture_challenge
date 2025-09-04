from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class SortablePage:
    URL = "https://demoqa.com/sortable"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def sort_list(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
        actions = ActionChains(self.driver)
        # Exemplo: mover último para a primeira posição
        actions.drag_and_drop(items[-1], items[0]).perform()
        return [i.text for i in self.driver.find_elements(By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")]
