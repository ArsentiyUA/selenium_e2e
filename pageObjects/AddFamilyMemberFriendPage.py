from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class FamilyMemberFriend:
    def __init__(self, driver):
        self.driver = driver

    first_name_element = (By.ID, 'id_first_name')
    last_name_element = (By.ID, 'id_last_name')
    email_element = (By.ID, 'id_email')
    phone_element = (By.ID, 'id_phone')
    address1_element = (By.ID, 'id_address_line1')
    address2_element = (By.ID, 'id_address_line2')
    id_city_element = (By.ID, 'id_city')
    zip_input_element = (By.ID, 'id_zip')
    gender_element = (By.ID, 'id_gender_1')
    submit_element = (By.CSS_SELECTOR, 'button[class="btn btn-primary btn-block btn-lg"]')

    def provide_first_name(self):
        return self.driver.find_element(*FamilyMemberFriend.first_name_element).send_keys("Arsentiy")

    def provide_last_name(self):
        return self.driver.find_element(*FamilyMemberFriend.last_name_element).send_keys("Abramov")

    def provide_email(self):
        return self.driver.find_element(*FamilyMemberFriend.email_element).send_keys("arsen@getaloecare.com")

    def provide_phone(self):
        return self.driver.find_element(*FamilyMemberFriend.phone_element).send_keys(9292579434)

    def select_relation(self):
        select_relation = Select(self.driver.find_element(By.NAME, 'relationship'))
        select_relation.select_by_visible_text('Son')

    def provide_address1(self):
        return self.driver.find_element(*FamilyMemberFriend.address1_element).send_keys("881 Rutland Rd")

    def provide_address2(self):
        return self.driver.find_element(*FamilyMemberFriend.address2_element).send_keys("2nd Floor")

    def provide_city(self):
        return self.driver.find_element(*FamilyMemberFriend.id_city_element).send_keys("Brooklyn")

    def select_state(self):
        select_state = Select(self.driver.find_element(By.NAME, 'state'))
        select_state.select_by_visible_text("New York")

    def provide_zip(self):
        return self.driver.find_element(*FamilyMemberFriend.zip_input_element).send_keys(11203)

    def choose_gender(self):
        return self.driver.find_element(*FamilyMemberFriend.gender_element).click()

    def submit(self):
        return self.driver.find_element(*FamilyMemberFriend.submit_element).click()


