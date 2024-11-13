import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page_recovery_page import PasswordRecoveryPage
from src.config import RESTORE_URL
from src.data import TEST_DATA



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
        assert page.wait_for_submit_recovery_button().is_displayed()

    def test_toggle_password_visibility(self, driver):
        page = PasswordRecoveryPage(driver)
        page.go_to_password_recovery(RESTORE_URL)
        page.toggle_password_visibility()

        assert page.is_password_field_highlighted() == True