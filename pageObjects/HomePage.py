from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    get_started_element = (By.LINK_TEXT, "Get Started, Risk-Free")

    def get_started_risk_free(self):
        return self.driver.find_element(*HomePage.get_started_element).click()
