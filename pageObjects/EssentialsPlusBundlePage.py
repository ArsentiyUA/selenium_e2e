from selenium.webdriver.common.by import By


class EssentialsPlusPage:
    def __init__(self, driver):
        self.driver = driver

    essentialsplus_order_now_element = (By.CSS_SELECTOR, 'a[href="https://store.aloecare.com/shop/products/72,73"]')

    def essentialsplus_order(self):
        return self.driver.find_element(*EssentialsPlusPage.essentialsplus_order_now_element).click()
