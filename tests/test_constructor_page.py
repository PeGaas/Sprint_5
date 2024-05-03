from selenium.webdriver.common.by import By
import locators


def test_move_on_toppings_by_click(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.TOPPINGS).click()

    assert 'tab_tab_type_current__2BEPc' in chrome_driver.find_element(By.XPATH, locators.TOPPINGS).get_attribute("class")


def test_move_on_sauces_by_click(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.SAUCES).click()

    assert 'tab_tab_type_current__2BEPc' in chrome_driver.find_element(By.XPATH, locators.SAUCES).get_attribute("class")


def test_move_on_buns_by_click(chrome_driver):
    chrome_driver.find_element(By.XPATH, locators.TOPPINGS).click()
    chrome_driver.find_element(By.XPATH, locators.BUNS).click()

    assert 'tab_tab_type_current__2BEPc' in chrome_driver.find_element(By.XPATH, locators.BUNS).get_attribute("class")
