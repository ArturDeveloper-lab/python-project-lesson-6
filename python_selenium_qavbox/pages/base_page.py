from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, by_location):
        # WebDriverWait(self.driver,10).untill(EC.presence_of_element_located(by_location)).click()
        self.wait.untill(EC.presence_of_element_located(by_location)).click()

    def send_keys(self, by_location, value):
        self.wait.untill(EC.presence_of_element_located(by_location)).send_keys(value)
        # self.wait.untill(EC.element_to_be_clickable(by_location)).send_keys(value)

    def get_text(self, by_location):
        return self.wait.untill(EC.visibility_of_element_located(by_location)).get_attribute("innerText")

    def wait_for(self, by_location):
        self.wait.until(EC.visibility_of_element_located(by_location))