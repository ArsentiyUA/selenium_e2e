from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class VerifyInfoService:
    def __init__(self, driver):
        self.driver = driver

    phone_element = (By.ID, 'id_phone')
    gender_element = (By.ID, 'id_gender_1')
    lockbox_element = (By.ID, 'id_lockbox_code')
    entry_instructions_element = (By.ID, 'id_lockbox_location')
    submit_element = (By.CSS_SELECTOR, 'button[class="btn btn-primary btn-block btn-lg"]')

    def provide_phone(self):
        return self.driver.find_element(*VerifyInfoService.phone_element).send_keys(9292579434)

    def select_dob(self):
        birth_date_month = Select(self.driver.find_element(By.NAME, 'birth_date_month'))
        birth_date_month.select_by_visible_text("June")
        birth_date_day = Select(self.driver.find_element(By.NAME, 'birth_date_day'))
        birth_date_day.select_by_visible_text("2")
        birth_date_year = Select(self.driver.find_element(By.NAME, 'birth_date_year'))
        birth_date_year.select_by_visible_text("1917")

    def choose_gender(self):
        return self.driver.find_element(*VerifyInfoService.gender_element).click()

    def provide_lockbox_info(self):
        return self.driver.find_element(*VerifyInfoService.lockbox_element).send_keys(0000)

    def provide_entry_instructions(self):
        return self.driver.find_element(*VerifyInfoService.entry_instructions_element).send_keys("under the carpet")

    def submit(self):
        return self.driver.find_element(*VerifyInfoService.submit_element).click()
