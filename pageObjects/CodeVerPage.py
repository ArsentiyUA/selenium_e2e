from selenium.webdriver.common.by import By


class CodeVer:
    def __init__(self, driver):
        self.driver = driver

    ver_code_element = (By.ID, 'id_code')
    submit_element = (By.CSS_SELECTOR, 'button[class="btn btn-primary btn-block btn-lg"]')

    def provide_code(self, code):
        return self.driver.find_element(*CodeVer.ver_code_element).send_keys(code)

    def submit(self):
        return self.driver.find_element(*CodeVer.submit_element).click()
