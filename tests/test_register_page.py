from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
import locators
import data_generator
from data import LOGIN_URL, PROFILE_URL


def test_registration_user_true(chrome_driver):
    email = data_generator.generate_email()
    password = data_generator.generate_password()
    name = data_generator.generate_name()

    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    chrome_driver.find_element(By.XPATH, locators.LINK_SIGN_UP).click()
    chrome_driver.find_element(By.XPATH, locators.FIELD_NAME_ON_SIGNUP_PAGE).send_keys(name)
    chrome_driver.find_element(By.XPATH, locators.FIELD_EMAIL_ON_SIGNUP_PAGE).send_keys(email)
    chrome_driver.find_element(By.XPATH, locators.FIELD_PASSWORD_ON_SIGNUP_PAGE).send_keys(password)
    chrome_driver.find_element(By.CSS_SELECTOR, locators.BUTTON_SIGN_UP_ON_REGISTER_PAGE).click()

    wait(chrome_driver, 5).until(EC.url_to_be(LOGIN_URL))
    chrome_driver.find_element(By.CSS_SELECTOR, locators.FIELD_EMAIL_ON_INPUT_PAGE).send_keys(email)
    chrome_driver.find_element(By.CSS_SELECTOR, locators.FIELD_PASSWORD_ON_INPUT_PAGE).send_keys(password)
    chrome_driver.find_element(By.CSS_SELECTOR, locators.BUTTON_INPUT).click()

    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    wait(chrome_driver, 5).until(EC.url_to_be(PROFILE_URL))

    profile_name = chrome_driver.find_element(By.XPATH, locators.FIELD_NAME_ON_PROFILE_PAGE).get_attribute('value')
    profile_email = chrome_driver.find_element(By.XPATH, locators.FIELD_EMAIL_ON_PROFILE_PAGE).get_attribute('value')

    assert profile_name == name and profile_email == email.lower()


def test_registration_user_with_password_less_then5_simbols(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    chrome_driver.find_element(By.XPATH, locators.LINK_SIGN_UP).click()
    chrome_driver.find_element(By.XPATH, locators.FIELD_NAME_ON_SIGNUP_PAGE).send_keys(data_generator.generate_name())
    chrome_driver.find_element(By.XPATH, locators.FIELD_EMAIL_ON_SIGNUP_PAGE).send_keys(data_generator.generate_email())
    chrome_driver.find_element(By.XPATH, locators.FIELD_PASSWORD_ON_SIGNUP_PAGE).send_keys(data_generator.generate_password_less_then5())
    chrome_driver.find_element(By.CSS_SELECTOR, locators.BUTTON_SIGN_UP_ON_REGISTER_PAGE).click()

    invalid_password_text = chrome_driver.find_element(By.CSS_SELECTOR, locators.TEXT_MESSAGE_INVALID_PASSWORD).text

    assert invalid_password_text == 'Некорректный пароль'
