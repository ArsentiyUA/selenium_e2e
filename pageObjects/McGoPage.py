from selenium.webdriver.common.by import By


class McGoPage:
    def __init__(self, driver):
        self.driver = driver

    mc_order_now_element = (By.CSS_SELECTOR, 'a[href="https://store.aloecare.com/shop/products/142,88"]')

    def mc_order(self):
        return self.driver.find_element(*McGoPage.mc_order_now_element).click()
