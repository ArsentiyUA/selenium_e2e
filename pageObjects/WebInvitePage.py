from selenium.webdriver.common.by import By
from utilities.BaseClass import generate_email


class WebInvite:
    def __init__(self, driver):
        self.driver = driver

    field_element = (By.CSS_SELECTOR, 'button[class="btn btn-block btn-info btn-lg"]')
    invite_element = (By.ID, 'id_email')
    send_invite_element = (By.CSS_SELECTOR, 'button[class="btn btn-primary btn-block btn-lg mt-5"]')

    def tap_on(self):
        return self.driver.find_element(*WebInvite.field_element).click()

    def provide_email_address(self, email_id=generate_email()):
        return self.driver.find_element(*WebInvite.invite_element).send_keys(email_id)

    def send_invite(self):
        return self.driver.find_element(*WebInvite.send_invite_element).click()
