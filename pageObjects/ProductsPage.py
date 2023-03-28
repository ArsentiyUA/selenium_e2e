from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    learn_more_mcgo_element = (By.CSS_SELECTOR, 'a[href="/products/mobile-companion"]')
    learn_more_essentials_element = (By.CSS_SELECTOR, 'a[href="/products/essentials"]')
    learn_more_essentials_plus_element = (By.CSS_SELECTOR, 'a[href="/products/essentials-plus"]')
    learn_more_totalcare_element = (By.CSS_SELECTOR, 'a[href="/products/total-care"]')

    def learn_more_mcgo(self):
        return self.driver.find_element(*ProductsPage.learn_more_mcgo_element).click()

    def learn_more_essentials(self):
        return self.driver.find_element(*ProductsPage.learn_more_essentials_element).click()

    def learn_more_essentialsplus(self):
        return self.driver.find_element(*ProductsPage.learn_more_essentials_plus_element).click()

    def learn_more_totalcare(self):
        return self.driver.find_element(*ProductsPage.learn_more_totalcare_element).click()
