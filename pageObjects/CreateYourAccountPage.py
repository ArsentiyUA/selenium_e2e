import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import generate_email


class CreateYourAccount:
    def __init__(self, driver):
        self.driver = driver

    first_name_element = (By.ID, 'id_first_name')
    last_name_element = (By.ID, 'id_last_name')
    email_element = (By.ID, 'id_email')
    password_element = (By.ID, '__BVID__3')
    checkbox_element = (By.CSS_SELECTOR, 'label[class="custom-control-label font-weight-bold"]')
    submit_element = (By.CSS_SELECTOR, 'button[class="btn btn-primary btn-block btn-lg"]')

    def provide_first_name(self):
        return self.driver.find_element(*CreateYourAccount.first_name_element).send_keys("Arsentiy")

    def provide_last_name(self):
        return self.driver.find_element(*CreateYourAccount.last_name_element).send_keys("Abramov")

    def provide_email(self, email_id=generate_email()):
        return self.driver.find_element(*CreateYourAccount.email_element).send_keys(email_id)

    def provide_password(self):
        return self.driver.find_element(*CreateYourAccount.password_element).send_keys("Test123!")

    def click_checkbox(self):
        return self.driver.find_element(*CreateYourAccount.checkbox_element).click()

    def click_submit(self):
        return self.driver.find_element(*CreateYourAccount.submit_element).click()



