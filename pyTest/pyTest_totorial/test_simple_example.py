import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def init_web_driver(request):
    print("\n in web driver init")
    driver:WebDriver
    browser_name = request.config.option.browser_name
    if browser_name =="chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox
    else: driver=webdriver.Chrome()


    yield driver
    print("I'm after the yield")
    driver.close()


@pytest.fixture()
def init_web_driver():
    print("\n in web driver init")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    print("I'm after the yield")
    driver.close()



# execute only onece in each test
# @pytest.fixture(scope="session")
# def second_fixture():
#     print("\n I'm inside the second fixture")
#     yield webdriver.Chrome(ChromeDriverManager().install())
#     print("I'm after the yield")


# @pytest.fixture(scope="module")
# def second_fixture():
#     print("\n I'm inside the second fixture")

# @pytest.fixture(scope="package")
# def second_fixture():
#     print("\n I'm inside the second fixture")

# @pytest.fixture(scope="class")
# def second_fixture():
#     print("\n I'm inside the second fixture")

# @pytest.fixture(scope="function")
# def second_fixture():
#     print("\n I'm inside the second fixture")

@pytest.mark.sanity
@pytest.mark.usefixtures("init_web_driver")
def test_my_first_one():
    print("\n I'm inside my first test")
    my_validation = True

    assert my_validation, "The validation of this test has failed"


# def test_my_second_one(init_web_driver):
#     driver = init_web_driver
#     driver.get("https://www.google.com/")
#     print("\n I'm inside my second test")
#     # pre-conditeon
#     # Test body
#     # Validation /expected result


def test_my_second_one(init_web_driver):
    driver: WebDriver = init_web_driver
    expected_url = "https://www.rainthedog.com/"
    driver.get(expected_url)
    actual_url = driver.current_url
    assert  expected_url == actual_url, "Expected url didn't match the actual"

    print("\n I'm inside my second test")
    # pre-conditeon
    # Test body
    # Validation /expected result



#     two way to use the init_web_driver() 1)@pytest.mark.usefixtures("init_web_driver")
#  def test_my_second_one(init_web_driver):
