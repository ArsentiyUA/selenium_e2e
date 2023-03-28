from selenium.webdriver.common.by import By


class EssentialsPage:
    def __init__(self, driver):
        self.driver = driver

    essentials_order_now_element = (By.CSS_SELECTOR, 'a[href="https://store.aloecare.com/shop/products/5,8"]')

    def essentials_order(self):
        return self.driver.find_element(*EssentialsPage.essentials_order_now_element).click()
