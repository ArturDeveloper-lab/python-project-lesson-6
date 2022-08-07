class LoginPage():

    # constractor  call evry time when call the class
    def __init__(self, driver):
        self.driver = driver

        self.username_textBox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.invalidUserName_message_xpath = "//span[@id='spanMessage']"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textBox_id).clear()
        self.driver.find_element_by_id( self.username_textBox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        msg = self.driver.find_element_by_xpath(self.login_button_id).text
        return msg

