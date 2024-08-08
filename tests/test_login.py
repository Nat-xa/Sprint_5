from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import StellarBurgersLocators
from settings import Settings


class TestLogin:

    def test_login_button_main(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_FIELD).send_keys(Settings.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_FIELD).send_keys(Settings.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()

        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.PLACE_AN_ORDER))
        place_an_order = driver.find_element(*StellarBurgersLocators.PLACE_AN_ORDER)

        assert place_an_order.is_displayed()

    def test_login_button_personal_account(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_FIELD).send_keys(Settings.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_FIELD).send_keys(Settings.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.PLACE_AN_ORDER))
        place_an_order = driver.find_element(*StellarBurgersLocators.PLACE_AN_ORDER)

        assert place_an_order.is_displayed()

    def test_login_button_form_registration(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_FORM_REGISTRATION).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_LINK_FORM_REGISTRATION).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_FIELD).send_keys(Settings.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_FIELD).send_keys(Settings.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.PLACE_AN_ORDER))
        place_an_order = driver.find_element(*StellarBurgersLocators.PLACE_AN_ORDER)

        assert place_an_order.is_displayed()

    def test_login_button_form_password_recovery(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_FORM_PASSWORD_RECOVERY).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_LINK_FORM_REGISTRATION).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_FIELD).send_keys(Settings.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_FIELD).send_keys(Settings.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.PLACE_AN_ORDER))
        place_an_order = driver.find_element(*StellarBurgersLocators.PLACE_AN_ORDER)

        assert place_an_order.is_displayed()
