from selenium.webdriver.common.by import By


class VerifyYourInfo:
    def __init__(self, driver):
        self.driver = driver

    gender_element = (By.ID, 'id_gender_1')
    submit = (By.CSS_SELECTOR, 'button[class="btn btn-primary btn-block btn-lg"]')

    def choose_gender(self):
        return self.driver.find_element(*VerifyYourInfo.gender_element).click()

    def click_submit(self):
        return self.driver.find_element(*VerifyYourInfo.submit).click()