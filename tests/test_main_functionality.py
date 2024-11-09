import pytest
from selenium import webdriver
from main_page import MainPage
from locators import Locators
from config import BASE_URL, TEST_DATA


@pytest.mark.usefixtures("driver")
class TestMainFunctionality:
    def test_click_constructor(self, driver):
        page = MainPage(driver)
        page.click_constructor()
        assert driver.current_url == BASE_URL

    def test_click_order_feed(self, driver):
        page = MainPage(driver)
        page.click_order_feed()
        assert driver.current_url == BASE_URL + "/order-feed"

    def test_ingredient_details_modal(self, driver):
        page = MainPage(driver)
        page.open_ingredient_details()
        assert page.is_ingredient_details_modal_displayed()
        page.close_ingredient_details()
        assert not page.is_ingredient_details_modal_displayed()

    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        initial_count = page.get_ingredient_counter_value()
        page.add_ingredient_to_order()
        assert page.get_ingredient_counter_value() == initial_count + 1

    def test_logged_in_user_can_place_order(self, driver):
        # Проверка, что пользователь залогинен
        page = MainPage(driver)
        assert page.is_logged_in(), "User is not logged in"

        # Переход к оформлению заказа
        page.proceed_to_checkout()
        assert page.is_order_confirmation_displayed()