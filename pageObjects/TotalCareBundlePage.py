from selenium.webdriver.common.by import By


class TotalCarePage:
    def __init__(self, driver):
        self.driver = driver

    totalcare_order_now_element = (By.CSS_SELECTOR, 'a[href="https://store.aloecare.com/shop/products/84,7"]')

    def totalcare_order(self):
        return self.driver.find_element(*TotalCarePage.totalcare_order_now_element).click()
