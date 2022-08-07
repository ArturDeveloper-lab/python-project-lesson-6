from telnetlib import EC

from selenium.webdriver.common.by import By


class LoginPage:

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class = 'button-1 login-button']"
    link_logout_linktext = "Logout"

    # textbox_username_id = (By.ID, "Email")
    # textbox_password_id = (By.ID, "Password")
    # button_login_xpath = (By.XPATH, "//button[@class = 'button-1 login-button']")
    # link_logout_linktext = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        # super().__init__(driver)
        self.driver = driver

    def login(self):
        self.action.send_keys(self.textbox_username_id, "aaaa")

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)


    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()


    def clickLogout(self):
        self.driver.find_element_by_id(self.link_logout_linktext).click()