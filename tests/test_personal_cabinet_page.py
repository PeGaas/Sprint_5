from selenium.webdriver.common.by import By
import locators


def test_open_personal_cabinet_on_click_personal_cabinet(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()

    assert chrome_driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_move_from_personal_cabinet_on_constructor_by_click(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    chrome_driver.find_element(By.XPATH, locators.CONSTRUCTOR).click()

    assert chrome_driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_move_from_personal_cabinet_on_logo_stellar_burgers_by_click(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    chrome_driver.find_element(By.XPATH, locators.LOGO_STELLAR_BURGERS).click()

    assert chrome_driver.current_url == 'https://stellarburgers.nomoreparties.site/'