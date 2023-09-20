import os
from selenium.webdriver.common.by import By

INPUT_CC = os.getenv("INPUT_CC")
INPUT_EXP = os.getenv("INPUT_EXP")
INPUT_CVC = os.getenv("INPUT_CVC")
INPUT_ZIP = os.getenv("INPUT_ZIP")



class BillingInfo:
    def __init__(self, driver):
        self.driver = driver

    credit_card_element = (By.CSS_SELECTOR, 'input[name="number"]')
    exp_element = (By.CSS_SELECTOR, 'input[name="expiry"]')
    cvc_element = (By.CSS_SELECTOR, 'input[name="cvc"]')
    zip_element = (By.CSS_SELECTOR, 'input[name="postalCode"]')
    submit_element = (By.CSS_SELECTOR, 'button[class="btn mt-5 animated fadeIn btn-primary btn-lg btn-block"]')

    def provide_cc_info(self):
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, 'iframe'))
        return self.driver.find_element(*BillingInfo.credit_card_element).send_keys(INPUT_CC)

    def provide_exp(self):
        return self.driver.find_element(*BillingInfo.exp_element).send_keys(INPUT_EXP)

    def provide_cvc(self):
        return self.driver.find_element(*BillingInfo.cvc_element).send_keys(INPUT_CVC)

    def provide_zip(self):
        return self.driver.find_element(*BillingInfo.zip_element).send_keys(INPUT_ZIP)

    def submit(self):
        self.driver.switch_to.default_content()
        return self.driver.find_element(*BillingInfo.submit_element).click()
