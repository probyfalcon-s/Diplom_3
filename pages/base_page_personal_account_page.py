from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class PersonalAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_personal_account(self, base_url):
        self.driver.get(base_url)
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(Locators.BUTTON_ACCOUNT)
        )

    def click_personal_account_button(self):
        self.driver.find_element(*Locators.BUTTON_ACCOUNT).click()

    def enter_email(self, email):
        self.driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    def enter_password(self, password):
        self.driver.find_element(*Locators.INPUT_PASSWORD_LOGIN).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*Locators.BUTTON_LOGIN).click()

    def go_to_order_history(self):
        self.driver.find_element(*Locators.SECTION_ORDER_HISTORY).click()

    def logout(self):
        self.driver.find_element(*Locators.BUTTON_LOGOUT).click()

    def is_order_history_displayed(self):
        return self.driver.find_element(*Locators.SECTION_ORDER_HISTORY).is_displayed()

    def is_logged_out(self):
        # Проверка, что кнопка входа на главной странице отображается
        return self.driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).is_displayed()