from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Actions:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def send_keys(self, by_locator, value):
        # self.wait.until(EC.element_to_be_clickable(by_locator)).send_keys(value)
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(value)


    def waitUntilElementVisibleClickJC(self,locator ,timeWait):
        WebDriverWait(self.driver, timeWait).until(EC.presence_of_element_located((By.ID, locator)))
        # element = self.driver.find_element_by_id(locator)
        self.driver.execute_script("arguments[0].click();", locator)
