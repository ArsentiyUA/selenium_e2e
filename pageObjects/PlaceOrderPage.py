from selenium.webdriver.common.by import By


class PlaceOrder:
    def __init__(self, driver):
        self.driver = driver

    place_order_elemenet = (By.CSS_SELECTOR, 'button[class="btn btn-info btn-lg btn-block"]')

    def place_order(self):
        return self.driver.find_element(*PlaceOrder.place_order_elemenet).click()
