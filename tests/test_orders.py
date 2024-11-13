import pytest
from selenium import webdriver
from pages.base_page_order_page import OrderFeedPage
from src.config import BASE_URL


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

        assert page.wait_for_total_completed_count_to_increase(initial_count)

    def test_today_completed_count_increases(self, driver):
        page = OrderFeedPage(driver)
        initial_today_count = page.get_today_completed_count()
        page.create_new_order()

        assert page.wait_for_today_completed_count_to_increase(initial_today_count)

    def test_order_appears_in_progress(self, driver):
        page = OrderFeedPage(driver)
        page.create_new_order()
        new_order_number = page.get_new_order_number()

        assert page.is_order_in_progress_displayed(new_order_number)