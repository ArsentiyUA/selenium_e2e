from selenium.webdriver.common.by import By


class PhoneNumberVer:
    def __init__(self, driver):
        self.driver = driver

    phone_element = (By.ID, 'id_phone')
    submit_element = (By.CSS_SELECTOR, 'button[class="btn btn-primary btn-block btn-lg"]')

    def provide_phone_number(self):
        return self.driver.find_element(*PhoneNumberVer.phone_element).send_keys(9292579434)

    def submit(self):
        return self.driver.find_element(*PhoneNumberVer.submit_element).click()