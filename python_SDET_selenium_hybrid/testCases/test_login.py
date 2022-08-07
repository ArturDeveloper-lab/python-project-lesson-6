from os.path import dirname

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.general_methods import getRootOfProject


# https://www.youtube.com/watch?v=y2Kz3QaZcVo
#
class Test_001_Login:

    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"
    baseURL = ReadConfig.getApplicationURL()
    print(baseURL)
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()



    # MAIN_DIRECTORY = dirname(dirname(__file__))
    def test_homePageTitle(self ,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            print(getRootOfProject() +"/Screenshots/" + "test_homePageTitle.png")
            self.driver.save_screenshot(getRootOfProject() +"/Screenshots/" + "test_homePageTitle.png")
            self.driver.close()
            assert False


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(getRootOfProject() +"/Screenshots/" + "test_login.png")
            self.driver.close()
            assert False


