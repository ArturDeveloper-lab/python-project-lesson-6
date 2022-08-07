import random
import time
from random import random
from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver


class Driver_factory_actions:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


def click(self, by_locator):
    WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).click()


def sendKeys(self, by_locator, value):
    WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).send_keys(value)


def clickJS(self, by_locator):
    WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(by_locator))


def rundomNumber():
    runNumber = random.randint(0, 22)
    return runNumber


def getText(self, by_locator):
    return by_locator.text


def isDisplayed(self, by_locator):
    by_locator.is_displayed()


def isSelected(self, by_locator):
    by_locator.is_selected()


def hover(self, by_locator):
    action = ActionChains(driver)
    action.move_to_element(by_locator).perform()


def closeTabs(self, by_locator):
    time.sleep(3)
    try:
        count = 0
        while count < 15:
            count = count + 1
            by_locator.click()
    except:
        print("not existing the open tabs\n")
