import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.LoginPage import LoginPage
from Pages.homePage import HomePage

# link to course in youtube
# https://www.youtube.com/watch?v=BURK7wMcCwU

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("-------------setup-------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    # driver.get("http://www.google.com")

    yield
    print("----------------tear down--------------")
    driver.quit()

def test_login(init_driver):
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()


def test_login_negative(init_driver):
    login = LoginPage(driver)
    login.enter_username("Admin1")
    login.enter_password("admin123")
    login.click_login()
    print(login.click_login())
    # self.assertEqual(login.click_login(), "Invalid credentials")