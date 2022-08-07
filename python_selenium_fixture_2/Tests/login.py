import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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

def test_login( init_driver):

        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_link_text("Logout").click()



