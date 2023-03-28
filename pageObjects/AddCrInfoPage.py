from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCrInfo:
    def __init__(self, driver):
        self.driver = driver

    first_name_element = (By.ID, 'id_first_name')
    last_name_element = (By.ID, 'id_last_name')
    phone_element = (By.ID, 'id_phone')
    address1_element = (By.ID, 'id_address_line1')
    address2_element = (By.ID, 'id_address_line2')
    id_city_element = (By.ID, 'id_city')
    zip_input_element = (By.ID, 'id_zip')
    gender_element = (By.ID, 'id_gender_1')
    lockbox_element = (By.ID, 'id_lockbox_code')
    entry_instructions_element = (By.ID, 'id_lockbox_location')
    submit_element = (By.CSS_SELECTOR, 'button[class="btn btn-primary btn-block btn-lg"]')

    def provide_first_name(self):
        return self.driver.find_element(*AddCrInfo.first_name_element).send_keys("Arsentiy")

    def provide_last_name(self):
        return self.driver.find_element(*AddCrInfo.last_name_element).send_keys("Abramov")

    def provide_phone(self):
        return self.driver.find_element(*AddCrInfo.phone_element).send_keys(9292579434)

    def provide_address1(self):
        return self.driver.find_element(*AddCrInfo.address1_element).send_keys("881 Rutland Rd")

    def provide_address2(self):
        return self.driver.find_element(*AddCrInfo.address2_element).send_keys("2nd Floor")

    def provide_city(self):
        return self.driver.find_element(*AddCrInfo.id_city_element).send_keys("Brooklyn")

    def select_state(self):
        select_state = Select(self.driver.find_element(By.NAME, 'state'))
        select_state.select_by_visible_text("New York")

    def provide_zip(self):
        return self.driver.find_element(*AddCrInfo.zip_input_element).send_keys(11203)

    def select_dob(self):
        birth_date_month = Select(self.driver.find_element(By.NAME, 'birth_date_month'))
        birth_date_month.select_by_visible_text("June")
        birth_date_day = Select(self.driver.find_element(By.NAME, 'birth_date_day'))
        birth_date_day.select_by_visible_text("2")
        birth_date_year = Select(self.driver.find_element(By.NAME, 'birth_date_year'))
        birth_date_year.select_by_visible_text("1917")

    def choose_gender(self):
        return self.driver.find_element(*AddCrInfo.gender_element).click()

    def select_relation(self):
        select_relationship = Select(self.driver.find_element(By.NAME, 'care_receiver_relationship'))
        select_relationship.select_by_visible_text("Son")

    def provide_lockbox_info(self):
        return self.driver.find_element(*AddCrInfo.lockbox_element).send_keys(0000)

    def provide_entry_instructions(self):
        return self.driver.find_element(*AddCrInfo.entry_instructions_element).send_keys("under the carpet")

    def submit(self):
        return self.driver.find_element(*AddCrInfo.submit_element).click()
