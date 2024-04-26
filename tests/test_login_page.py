from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
import locators

import data


def test_login_button_sign_in_to_account_on_home_page(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.BUTTON_SIGNIN_ON_HOME_PAGE).click()
    wait(chrome_driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    assert chrome_driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_login_button_personal_cabinet(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    wait(chrome_driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    assert chrome_driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_login_button_on_registration_page(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    chrome_driver.find_element(By.XPATH, locators.LINK_SIGN_UP).click()
    chrome_driver.find_element(By.XPATH, locators.LINK_SIGNIN_ON_REGISTER_PAGE).click()
    wait(chrome_driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    assert chrome_driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_login_button_on_forgot_password_page(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    chrome_driver.find_element(By.XPATH, locators.LINK_FORGOT_PASSWORD_ON_REGISTER_PAGE).click()
    chrome_driver.find_element(By.XPATH, locators.LINK_SIGNIN_ON_FORGOT_PASSWORD_PAGE).click()
    wait(chrome_driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    assert chrome_driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_exit_from_personal_cabinet_click_button_exit(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    chrome_driver.find_element(By.XPATH, locators.LINK_SIGN_UP).click()
    chrome_driver.find_element(By.XPATH, locators.FIELD_NAME_ON_SIGNUP_PAGE).send_keys(data.NAME)
    chrome_driver.find_element(By.XPATH, locators.FIELD_EMAIL_ON_SIGNUP_PAGE).send_keys(data.EMAIL)
    chrome_driver.find_element(By.XPATH, locators.FIELD_PASSWORD_ON_SIGNUP_PAGE).send_keys(data.PASSWORD)
    chrome_driver.find_element(By.XPATH, locators.BUTTON_SIGN_UP_ON_REGISTER_PAGE).click()

    wait(chrome_driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
    chrome_driver.find_element(By.XPATH, locators.FIELD_EMAIL_ON_INPUT_PAGE).send_keys(data.EMAIL)
    chrome_driver.find_element(By.XPATH, locators.FIELD_PASSWORD_ON_INPUT_PAGE).send_keys(data.PASSWORD)
    chrome_driver.find_element(By.XPATH, locators.BUTTON_INPUT).click()

    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    wait(chrome_driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

    chrome_driver.find_element(By.XPATH, locators.EXIT_BUTTON).click()
    wait(chrome_driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    assert chrome_driver.current_url == 'https://stellarburgers.nomoreparties.site/login'




