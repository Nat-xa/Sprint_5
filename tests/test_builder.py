from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import StellarBurgersLocators
from settings import Settings


class TestBuilder:

    def test_builder_section_toppings(self, driver):
        section_toppings = driver.find_element(*StellarBurgersLocators.SECTION_TOPPINGS)
        section_toppings.click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.TAB_INDICATOR_TOPPINGS))
        indicator_toppings = driver.find_element(*StellarBurgersLocators.TAB_INDICATOR_TOPPINGS)
        title_topping = driver.find_element(*StellarBurgersLocators.TITLE_TOPPINGS)
        assert indicator_toppings.is_displayed() and title_topping.is_displayed()

    def test_builder_section_bread(self, driver):
        driver.find_element(*StellarBurgersLocators.SECTION_TOPPINGS).click()
        section_bread = driver.find_element(*StellarBurgersLocators.SECTION_BREAD)
        section_bread.click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.TAB_INDICATOR_BREAD))
        indicator_bread = driver.find_element(*StellarBurgersLocators.TAB_INDICATOR_BREAD)
        title_bread = driver.find_element(*StellarBurgersLocators.TITLE_BREAD)
        assert indicator_bread.is_displayed() and title_bread.is_displayed()

    def test_builder_section_sauces(self, driver):
        section_sauces = driver.find_element(*StellarBurgersLocators.SECTION_SAUCES)
        section_sauces.click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.TAB_INDICATOR_SAUCES))
        indicator_sauces = driver.find_element(*StellarBurgersLocators.TAB_INDICATOR_SAUCES)
        title_sauces = driver.find_element(*StellarBurgersLocators.TITLE_SAUCES)
        assert indicator_sauces.is_displayed() and title_sauces.is_displayed()
