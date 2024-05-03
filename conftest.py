import pytest
from selenium import webdriver
from data import MAIN_URL


@pytest.fixture()
def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()

