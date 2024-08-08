from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import StellarBurgersLocators
from settings import Settings


class TestLogout:

    def test_logout(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_INPUT_FIELD).send_keys(Settings.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_INPUT_FIELD).send_keys(Settings.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN_FORM).click()

        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.PLACE_AN_ORDER))
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.NAME_FIELD))
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, Settings.WAIT_TIME).until(EC.visibility_of_element_located
                                                        (StellarBurgersLocators.HEADER_ENTRY))
        header_entry = driver.find_element(*StellarBurgersLocators.HEADER_ENTRY)
        assert header_entry.is_displayed()
