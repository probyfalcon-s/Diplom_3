from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators

class OrderFeedPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def open_order_details(self):
        self.driver.find_element(*Locators.ORDER_ITEM).click()
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(Locators.ORDER_DETAILS_MODAL)
        )

    def close_order_details(self):
        self.driver.find_element(*Locators.MODAL_CLOSE_BUTTON).click()

    def is_order_details_modal_displayed(self):
        return self.driver.find_element(*Locators.ORDER_DETAILS_MODAL).is_displayed()

    def get_total_completed_count(self):
        return int(self.driver.find_element(*Locators.TOTAL_COMPLETED_COUNT).text)

    def get_today_completed_count(self):
        return int(self.driver.find_element(*Locators.TODAY_COMPLETED_COUNT).text)

    def create_new_order(self):
        self.driver.find_element(*Locators.BUTTON_CREATE_ORDER).click()

    def is_user_order_history_displayed(self):
        return self.driver.find_element(*Locators.USER_ORDER_HISTORY).is_displayed()

    def get_new_order_number(self):
        order_number_element = self.driver.find_element(*Locators.ORDER_NUMBER)
        return order_number_element.text

    def wait_for_order_in_progress(self, order_number):
        return self.wait.until(
            lambda d: self.is_order_in_progress_displayed(order_number)
        )

    def wait_for_today_completed_count_to_increase(self, initial_count):
        return self.wait.until(lambda d: self.get_today_completed_count() == initial_count + 1)

    def is_order_in_progress_displayed(self, order_number):
        orders_in_progress = self.driver.find_elements(*Locators.ORDER_NUMBER)
        return any(order.text == order_number for order in orders_in_progress)