import pytest
from selenium import webdriver
# from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


