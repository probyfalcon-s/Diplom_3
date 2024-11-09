from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class OrderFeedPage:
    def __init__(self, driver):
        self.driver = driver

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

    def is_order_in_progress_displayed(self, order_number):
        orders_in_progress = self.driver.find_elements(*Locators.ORDER_NUMBER)
        return any(order.text == order_number for order in orders_in_progress)