from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait

import locators


def test_move_on_toppings_by_click(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.TOPPINGS).click()

    assert wait(chrome_driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.TEXT_TOPPINGS)))


def test_move_on_sauces_by_click(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.TOPPINGS).click()
    wait(chrome_driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.TEXT_TOPPINGS)))
    chrome_driver.find_element(By.XPATH, locators.SAUCES).click()

    assert wait(chrome_driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.TEXT_SAUCES)))


def test_move_on_buns_by_click(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.TOPPINGS).click()
    wait(chrome_driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.TEXT_TOPPINGS)))
    chrome_driver.find_element(By.XPATH, locators.BUNS).click()

    assert wait(chrome_driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.TEXT_BUNS)))
