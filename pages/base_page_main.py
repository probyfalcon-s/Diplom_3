from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver import ActionChains

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def click_constructor(self):
        self.driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()

    def click_order_feed(self):
        self.driver.find_element(*Locators.BUTTON_ORDER_FEED).click()

    def open_ingredient_details(self):
        self.driver.find_element(*Locators.INGREDIENT_ITEM).click()
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(Locators.INGREDIENT_DETAILS_MODAL)
        )

    def close_ingredient_details(self):
        self.driver.find_element(*Locators.MODAL_CLOSE_BUTTON).click()

    def perform_drag_and_drop(self):
        source_element = self.driver.find_element(*Locators.BUTTON_ADD_TO_ORDER)
        target_element = self.driver.find_element(*Locators.TARGET_ELEMENT)

        # Выполняем drag-and-drop
        self.actions.drag_and_drop(source_element, target_element).perform()

    def get_ingredient_counter_value(self):
        return int(self.driver.find_element(*Locators.INGREDIENT_COUNTER).text)

    def proceed_to_checkout(self): #here
        self.driver.find_element(*Locators.BUTTON_CHECKOUT).click()

    def is_logged_in(self):
        return not self.driver.find_elements(*Locators.LOGIN_PROMPT)

    def is_order_confirmation_displayed(self):
        return self.driver.find_element(*Locators.ORDER_CONFIRMATION_MESSAGE).is_displayed()

    def is_ingredient_details_modal_displayed(self):
        return self.driver.find_element(*Locators.ORDER_CONFIRMATION_MESSAGE).is_displayed()