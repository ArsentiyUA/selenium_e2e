from selenium.webdriver.common.by import By


class ReviewYourOrder:
    def __init__(self, driver):
        self.driver = driver

    ContinueToCheckout = (By.CSS_SELECTOR, "button[class='btn btn-info btn-lg btn-block my-4']")

    def reviewyourorder(self):
        return self.driver.find_element(*ReviewYourOrder.ContinueToCheckout).click()
