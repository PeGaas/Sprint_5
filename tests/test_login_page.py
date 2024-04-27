from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
import data_generator
import locators
from data import LOGIN_URL, PROFILE_URL


def test_login_button_sign_in_to_account_on_home_page(chrome_driver):
    chrome_driver.find_element(By.CSS_SELECTOR, locators.BUTTON_SIGNIN_ON_HOME_PAGE).click()
    wait(chrome_driver, 5).until(EC.url_to_be(LOGIN_URL))

    assert chrome_driver.current_url == LOGIN_URL


def test_login_button_personal_cabinet(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    wait(chrome_driver, 5).until(EC.url_to_be(LOGIN_URL))

    assert chrome_driver.current_url == LOGIN_URL


def test_login_button_on_registration_page(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    chrome_driver.find_element(By.XPATH, locators.LINK_SIGN_UP).click()
    chrome_driver.find_element(By.CSS_SELECTOR, locators.LINK_SIGNIN_ON_REGISTER_PAGE).click()
    wait(chrome_driver, 5).until(EC.url_to_be(LOGIN_URL))

    assert chrome_driver.current_url == LOGIN_URL


def test_login_button_on_forgot_password_page(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.PERSONAL_CABINET).click()
    chrome_driver.find_element(By.XPATH, locators.LINK_FORGOT_PASSWORD_ON_REGISTER_PAGE).click()
    chrome_driver.find_element(By.CSS_SELECTOR, locators.LINK_SIGNIN_ON_FORGOT_PASSWORD_PAGE).click()
    wait(chrome_driver, 5).until(EC.url_to_be(LOGIN_URL))

    assert chrome_driver.current_url == LOGIN_URL


def test_exit_from_personal_cabinet_click_button_exit(chrome_driver):
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

    chrome_driver.find_element(By.CSS_SELECTOR, locators.EXIT_BUTTON).click()
    wait(chrome_driver, 5).until(EC.url_to_be(LOGIN_URL))

    assert chrome_driver.current_url == LOGIN_URL




