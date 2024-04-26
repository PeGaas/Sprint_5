from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
import locators

import data


def test_registration_user_true(chrome_driver):
    email = data.generate_email()
    password = data.generate_password()
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    chrome_driver.find_element(By.XPATH, locators.LINK_SIGN_UP).click()
    chrome_driver.find_element(By.XPATH, locators.FIELD_NAME_ON_SIGNUP_PAGE).send_keys(data.NAME)
    chrome_driver.find_element(By.XPATH, locators.FIELD_EMAIL_ON_SIGNUP_PAGE).send_keys(email)
    chrome_driver.find_element(By.XPATH, locators.FIELD_PASSWORD_ON_SIGNUP_PAGE).send_keys(password)
    chrome_driver.find_element(By.XPATH, locators.BUTTON_SIGN_UP_ON_REGISTER_PAGE).click()

    wait(chrome_driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
    chrome_driver.find_element(By.XPATH, locators.FIELD_EMAIL_ON_INPUT_PAGE).send_keys(email)
    chrome_driver.find_element(By.XPATH, locators.FIELD_PASSWORD_ON_INPUT_PAGE).send_keys(password)
    chrome_driver.find_element(By.XPATH, locators.BUTTON_INPUT).click()

    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    wait(chrome_driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

    profile_name = chrome_driver.find_element(By.XPATH, locators.FIELD_NAME_ON_PROFILE_PAGE).get_attribute('value')
    profile_email = chrome_driver.find_element(By.XPATH, locators.FIELD_EMAIL_ON_PROFILE_PAGE).get_attribute('value')

    assert profile_name == data.NAME and profile_email == email.lower()


def test_registration_user_with_password_less_then5_simbols(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    chrome_driver.find_element(By.XPATH, locators.LINK_SIGN_UP).click()
    chrome_driver.find_element(By.XPATH, locators.FIELD_NAME_ON_SIGNUP_PAGE).send_keys(data.NAME)
    chrome_driver.find_element(By.XPATH, locators.FIELD_EMAIL_ON_SIGNUP_PAGE).send_keys(data.EMAIL)
    chrome_driver.find_element(By.XPATH, locators.FIELD_PASSWORD_ON_SIGNUP_PAGE).send_keys(data.INVALID_PASSWORD)
    chrome_driver.find_element(By.XPATH, locators.BUTTON_SIGN_UP_ON_REGISTER_PAGE).click()

    invalid_password_text = chrome_driver.find_element(By.XPATH, locators.TEXT_MESSAGE_INVALID_PASSWORD).text

    assert invalid_password_text == 'Некорректный пароль'
