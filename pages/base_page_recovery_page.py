from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators


class PasswordRecoveryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def go_to_password_recovery(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(Locators.BUTTON_RECOVER_PASSWORD)
        )

    def click_recover_password(self):
        self.driver.find_element(*Locators.BUTTON_RECOVER_PASSWORD).click()

    def enter_email(self, email):
        self.driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)

    def submit_recovery(self):
        self.driver.find_element(*Locators.BUTTON_SUBMIT_RECOVERY).click()

    def enter_password(self, password):
        self.driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)

    def enter_code(self, code):
        self.driver.find_element(*Locators.INPUT_CODE).send_keys(password)

    def toggle_password_visibility(self):
        self.driver.find_element(*Locators.INPUT_ACVIVE).click()

    def click_save(self):
        self.driver.find_element(*Locators.BUTTON_SAVE).click()


    def is_password_field_highlighted(self):
        # Проверка, что поле подсвечивается
        element = self.driver.find_element(*Locators.INPUT_ACVIVE)
        return 'highlight' in element.get_attribute('class')

    def wait_for_submit_recovery_button(self):
        # Ожидание видимости кнопки подтверждения восстановления пароля
        return self.wait.until(
            EC.visibility_of_element_located(Locators.BUTTON_SUBMIT_RECOVERY)
        )