from selenium.webdriver.common.by import By


class InstallSystem:
    def __init__(self, driver):
        self.driver = driver

    popup_element = (By.CSS_SELECTOR, 'button[class="btn btn-block btn-info btn-lg"]')
    option1_element = (By.ID, 'radioOption1')
    option2_element = (By.ID, 'radioOption2')
    submit_element = (By.CSS_SELECTOR, 'button[class="btn btn-primary btn-block btn-lg"]')

    def click_on_popup(self):
        return self.driver.find_element(*InstallSystem.popup_element).click()

    def choose_option1(self):
        return self.driver.find_element(*InstallSystem.option1_element).click()

    def choose_option2(self):
        return self.driver.find_element(*InstallSystem.option2_element).click()

    def submit(self):
        return self.driver.find_element(*InstallSystem.submit_element).click()