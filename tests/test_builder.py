from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import StellarBurgersLocators
from settings import Settings


class TestBuilder:

    def test_builder_section_toppings(self, driver):
        section_toppings = driver.find_element(*StellarBurgersLocators.SECTION_TOPPINGS)
        section_toppings.click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.ELEMENT_TOPPINGS))
        element_toppings = driver.find_element(*StellarBurgersLocators.ELEMENT_TOPPINGS)
        assert element_toppings.is_displayed()

    def test_builder_section_bread(self, driver):
        driver.find_element(*StellarBurgersLocators.SECTION_TOPPINGS).click()
        section_bread = driver.find_element(*StellarBurgersLocators.SECTION_BREAD)
        section_bread.click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.ELEMENT_BREAD))
        element_bread = driver.find_element(*StellarBurgersLocators.ELEMENT_BREAD)
        assert element_bread.is_displayed()

    def test_builder_section_sauces(self, driver):
        section_sauces = driver.find_element(*StellarBurgersLocators.SECTION_SAUCES)
        section_sauces.click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.ELEMENT_SAUCES))
        element_sauces = driver.find_element(*StellarBurgersLocators.ELEMENT_SAUCES)
        assert element_sauces.is_displayed()
