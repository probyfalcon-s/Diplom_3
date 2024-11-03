from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.data import TEST_DATA
from config.config import BASE_URL
from locators.locators import Locators

class TestNavigationToAccount:
    def test_move_personal_account_true(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*Locators.BUTTON_ACCOUNT).click()

        driver.find_element(*Locators.INPUT_EMAIL_LOGIN).send_keys(TEST_DATA['login'])
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(TEST_DATA['password'])
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_ORDER)))

        section_header = driver.find_element(*Locators.BUTTON_ORDER)
        assert section_header.is_displayed()

    def test_move_personal_account_to_constructor_true(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*Locators.BUTTON_ACCOUNT).click()

        driver.find_element(*Locators.INPUT_EMAIL_LOGIN).send_keys(TEST_DATA['login'])
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(TEST_DATA['password'])
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_ORDER)))

        driver.find_element(*Locators.BUTTON_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.HEADER_MAKE_BURGER)))

        assert driver.find_element(*Locators.HEADER_MAKE_BURGER).is_displayed()

    def test_move_personal_account_to_logo_true(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*Locators.BUTTON_ACCOUNT).click()

        driver.find_element(*Locators.INPUT_EMAIL_LOGIN).send_keys(TEST_DATA['login'])
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(TEST_DATA['password'])
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_ORDER)))

        driver.find_element(*Locators.BUTTON_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.HEADER_MAKE_BURGER)))

        section_header = driver.find_element(*Locators.HEADER_MAKE_BURGER)
        assert section_header.is_displayed()

    def test_move_personal_account_to_logout_true(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*Locators.BUTTON_ACCOUNT).click()

        driver.find_element(*Locators.INPUT_EMAIL_LOGIN).send_keys(TEST_DATA['login'])
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(TEST_DATA['password'])
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_ORDER)))

        driver.find_element(*Locators.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LINK_PROFILE)))
        driver.find_element(*Locators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LABEL_ENTER)))

        section_header = driver.find_element(*Locators.LABEL_ENTER)
        assert section_header.is_displayed()