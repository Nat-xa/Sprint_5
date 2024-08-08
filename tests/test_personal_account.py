from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import StellarBurgersLocators
from settings import Settings


class TestPersonalAccount:

    def test_personal_account(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_FIELD).send_keys(Settings.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_FIELD).send_keys(Settings.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()

        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.PLACE_AN_ORDER))
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.NAME_FIELD))
        name_field = driver.find_element(*StellarBurgersLocators.NAME_FIELD)
        assert name_field.is_displayed()

    def test_builder_from_personal_account(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_FIELD).send_keys(Settings.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_FIELD).send_keys(Settings.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()

        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.PLACE_AN_ORDER))
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.NAME_FIELD))
        driver.find_element(*StellarBurgersLocators.BUILDER).click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.PLACE_AN_ORDER))
        place_an_order = driver.find_element(*StellarBurgersLocators.PLACE_AN_ORDER)

        assert place_an_order.is_displayed()
