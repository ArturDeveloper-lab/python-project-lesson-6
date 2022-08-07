import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time





def test_art():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_link_text("Logout").click()


    # @pytest.fixture(scope='module')
    # def setup(self):
    #     self.driver = webdriver.Chrome(ChromeDriverManager().install())
    #     self.driver.implicitly_wait(10)
    #     self.driver.maximize_window()
    #
    # def test_login(self,setup):
    #     self.driver = setup
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/")
    #     self.driver.find_element_by_id("txtUsername").send_keys("Admin")
    #     self.driver.find_element_by_id("txtPassword").send_keys("admin123")
    #     self.driver.find_element_by_id("btnLogin").click()
    #     self.driver.find_element_by_id("welcome").click()
    #     self.driver.find_element_by_link_text("Logout").click()
    #
    #     time.sleep(2)
    #
    # def tests_tearDownClass(self,setup):
    #     self.driver.close()
    #     self.driver.quit()
    #     print("Test completed")
