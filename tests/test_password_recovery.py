import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from password_recovery_page import PasswordRecoveryPage
from locators import Locators
from config import RESTORE_URL, TEST_DATA



@pytest.mark.usefixtures("driver")
class TestPasswordRecovery:
    def test_password_recovery_navigation(self, driver):
        page = PasswordRecoveryPage(driver)
        page.go_to_password_recovery(RESTORE_URL)
        page.click_recover_password()
        assert driver.current_url == RESTORE_URL

    def test_email_input_and_submit(self, driver):
        page = PasswordRecoveryPage(driver)
        page.go_to_password_recovery(RESTORE_URL)
        page.click_recover_password()
        page.enter_email(TEST_DATA['login'])
        page.submit_recovery()

        # Проверка, что восстановление прошло успешно
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.BUTTON_SUBMIT_RECOVERY)
        )
        assert driver.find_element(*Locators.BUTTON_SUBMIT_RECOVERY).is_displayed()

    def test_toggle_password_visibility(self, driver):
        page = PasswordRecoveryPage(driver)
        page.go_to_password_recovery(RESTORE_URL)
        page.toggle_password_visibility()

        assert page.is_password_field_highlighted() == True