from selenium.webdriver.common.by import By

class WebTablesPage:
    URL = "https://demoqa.com/webtables"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def add_record(self, first_name, last_name, email, age, salary, department):
        self.driver.find_element(By.ID, "addNewRecordButton").click()
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)
        self.driver.find_element(By.ID, "age").send_keys(str(age))
        self.driver.find_element(By.ID, "salary").send_keys(str(salary))
        self.driver.find_element(By.ID, "department").send_keys(department)
        self.driver.find_element(By.ID, "submit").click()

    def edit_record(self, index, new_salary):
        self.driver.find_element(By.ID, f"edit-record-{index}").click()
        salary_field = self.driver.find_element(By.ID, "salary")
        salary_field.clear()
        salary_field.send_keys(str(new_salary))
        self.driver.find_element(By.ID, "submit").click()

    def delete_record(self, index):
        self.driver.find_element(By.ID, f"delete-record-{index}").click()
