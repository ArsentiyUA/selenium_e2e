from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ShippingInfo:
    def __init__(self, driver):
        self.driver = driver

    first_name_element = (By.ID, 'id_first_name')
    last_name_element = (By.ID, 'id_last_name')
    address_line1_element = (By.ID, 'id_address_line1')
    address_line2_element = (By.ID, 'id_address_line2')
    city_element = (By.ID, 'id_city')
    zip_input_element = (By.ID, 'id_zip')
    phone_number_element = (By.ID, 'id_phone')
    submit_element = (By.CSS_SELECTOR, 'button[class="btn btn-info btn-block btn-lg"]')

    def provide_first_name(self):
        return self.driver.find_element(*ShippingInfo.first_name_element).send_keys("Arsentiy")

    def provide_last_name(self):
        return self.driver.find_element(*ShippingInfo.last_name_element).send_keys("Abramov")

    def provide_address1(self):
        return self.driver.find_element(*ShippingInfo.address_line1_element).send_keys("881 Rutland Rd")

    def provide_address2(self):
        return self.driver.find_element(*ShippingInfo.address_line2_element).send_keys("2nd Floor")

    def provide_city(self):
        return self.driver.find_element(*ShippingInfo.city_element).send_keys("Brooklyn")

    def select_state(self):
        select_state = Select(self.driver.find_element(By.NAME, 'state'))
        select_state.select_by_visible_text("New York")

    def provide_zip(self):
        return self.driver.find_element(*ShippingInfo.zip_input_element).send_keys(11203)

    def provide_phone_number(self):
        return self.driver.find_element(*ShippingInfo.phone_number_element).send_keys(9292579434)

    def submit(self):
        return self.driver.find_element(*ShippingInfo.submit_element).click()
