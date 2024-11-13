import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page_personal_account_page import PersonalAccountPage
from src.config import BASE_URL


@pytest.mark.usefixtures("driver")
class TestPersonalAccount:
    def test_navigate_to_personal_account(self, driver):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account(BASE_URL)
        page.click_personal_account_button()
        page.enter_email(TEST_DATA['login'])
        page.enter_password(TEST_DATA['password'])
        page.click_login_buttom()
        assert driver.current_url == LOGIN_URL

    def test_navigate_to_order_history(self, driver):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account(BASE_URL)
        page.click_personal_account_button()
        page.enter_email(TEST_DATA['login'])
        page.enter_password(TEST_DATA['password'])
        page.click_login_buttom()
        page.go_to_order_history()

        # Проверка, что раздел "История заказов" отображается
        assert page.is_order_history_displayed()

    def test_logout(self, driver):
        page = PersonalAccountPage(driver)
        page.go_to_personal_account(BASE_URL)
        page.click_personal_account_button()
        page.enter_email(TEST_DATA['login'])
        page.enter_password(TEST_DATA['password'])
        page.click_login_buttom()
        page.logout()

        # Проверка, что после выхода отображается кнопка входа
        assert page.is_logged_out()