from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from helpers import Help
from locators import StellarBurgersLocators


class TestRegistration:

    def test_registration_valid_data(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_FORM_REGISTRATION).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(StellarBurgersLocators.
                                                                                     REGISTRATION_FORM))
        driver.find_element(*StellarBurgersLocators.REGISTRATION_FORM_NAME).send_keys("Natali")
        driver.find_element(*StellarBurgersLocators.REGISTRATION_FORM_EMAIL).send_keys(Help.generate_valid_email())
        driver.find_element(*StellarBurgersLocators.REGISTRATION_FORM_PASSWORD).send_keys(Help.generate_valid_password())
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(StellarBurgersLocators.
                                                                                     LOGIN_BUTTON_MAIN_FORM))
        login_button = driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM)
        assert login_button.is_displayed()

    def test_registration_not_valid_data(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_FORM_REGISTRATION).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(StellarBurgersLocators.
                                                                                     REGISTRATION_FORM))
        driver.find_element(*StellarBurgersLocators.REGISTRATION_FORM_NAME).send_keys("Natali")
        driver.find_element(*StellarBurgersLocators.REGISTRATION_FORM_EMAIL).send_keys(Help.generate_valid_email())
        driver.find_element(*StellarBurgersLocators.REGISTRATION_FORM_PASSWORD).send_keys(Help.
                                                                                          generate_not_valid_password())
        driver.find_element(*StellarBurgersLocators.REGISTRATION_FORM_NAME).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(StellarBurgersLocators.
                                                                                     PASSWORD_INPUT_ERROR))
        password_error = driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_ERROR)
        assert password_error.is_displayed()