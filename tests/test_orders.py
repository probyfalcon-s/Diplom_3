import pytest
from selenium import webdriver
from order_feed_page import OrderFeedPage
from locators import Locators
from config import BASE_URL



@pytest.mark.usefixtures("driver")
class TestOrderFeed:
    def test_order_details_modal(self, driver):
        page = OrderFeedPage(driver)
        page.open_order_details()
        assert page.is_order_details_modal_displayed()
        page.close_order_details()
        assert not page.is_order_details_modal_displayed()

    def test_user_order_history_displayed(self, driver):
        page = OrderFeedPage(driver)
        assert page.is_user_order_history_displayed()

    def test_total_completed_count_increases(self, driver):
        page = OrderFeedPage(driver)
        initial_count = page.get_total_completed_count()
        page.create_new_order()
        WebDriverWait(driver, 3).until(
            lambda d: page.get_total_completed_count() == initial_count + 1
        )

    def test_today_completed_count_increases(self, driver):
        page = OrderFeedPage(driver)
        initial_today_count = page.get_today_completed_count()
        page.create_new_order()
        WebDriverWait(driver, 3).until(
            lambda d: page.get_today_completed_count() == initial_today_count + 1
        )

    def test_order_appears_in_progress(self, driver):
        page = OrderFeedPage(driver)
        page.create_new_order()
        new_order_number = page.driver.find_element(*Locators.ORDER_NUMBER).text
        WebDriverWait(driver, 3).until(
            lambda d: page.is_order_in_progress_displayed(new_order_number)
        )
        assert page.is_order_in_progress_displayed(new_order_number)