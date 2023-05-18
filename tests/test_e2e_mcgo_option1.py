import time
from selenium.webdriver.common.by import By
from pageObjects.AddCrInfoPage import AddCrInfo
from pageObjects.BillingInfoPage import BillingInfo
from pageObjects.CodeVerPage import CodeVer
from pageObjects.CreateYourAccountPage import CreateYourAccount
from pageObjects.HomePage import HomePage
from pageObjects.McGoPage import McGoPage
from pageObjects.PhoneNumberVerPage import PhoneNumberVer
from pageObjects.PlaceOrderPage import PlaceOrder
from pageObjects.ProductsPage import ProductsPage
from pageObjects.ReviewYourOrderPage import ReviewYourOrder
from pageObjects.ShippingInfoPage import ShippingInfo
from pageObjects.VerifyYourInfoPage import VerifyYourInfo
from pageObjects.WebInvitePage import WebInvite
from pageObjects.WhereSystemPage import InstallSystem
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_get_started(self):
        log = self.getlogger()
        get_started_with_order = HomePage(self.driver)
        get_started_with_order.get_started_risk_free()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Products | Aloe Care Health | Medical alert system for Seniors with options for fall detection" in get_title)

    def test_choose_product(self):
        log = self.getlogger()
        choose_mc = ProductsPage(self.driver)
        choose_mc.learn_more_mcgo()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Mobile Companion Go | Aloe Care Health: Medical Alert for Seniors, Caregivers. Fall detection options." in get_title)

    def test_mc_product(self):
        log = self.getlogger()
        mc_go = McGoPage(self.driver)
        mc_go.mc_order()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Mobile Companion Go | Aloe Care Health: Medical Alert for Seniors, Caregivers. Fall detection options." in get_title)

    def test_review_order(self):
        log = self.getlogger()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        review_order = ReviewYourOrder(self.driver)
        review_order.reviewyourorder()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Sign Up | Aloe Care Health" in get_title)

    def test_create_account(self):
        log = self.getlogger()
        first_name = CreateYourAccount(self.driver)
        first_name.provide_first_name()
        last_name = CreateYourAccount(self.driver)
        last_name.provide_last_name()
        email = CreateYourAccount(self.driver)
        email.provide_email()
        password = CreateYourAccount(self.driver)
        password.provide_password()
        checkbox = CreateYourAccount(self.driver)
        checkbox.click_checkbox()
        submit = CreateYourAccount(self.driver)
        submit.click_submit()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Billing Information | Aloe Care Health" in get_title)

    def test_billing_info(self):
        log = self.getlogger()
        time.sleep(2)
        cc_input = BillingInfo(self.driver)
        cc_input.provide_cc_info()
        exp_input = BillingInfo(self.driver)
        exp_input.provide_exp()
        cvc_input = BillingInfo(self.driver)
        cvc_input.provide_cvc()
        zip_input = BillingInfo(self.driver)
        zip_input.provide_zip()
        submit = BillingInfo(self.driver)
        submit.submit()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Billing Information | Aloe Care Health" in get_title)

    def test_shipping_info(self):
        log = self.getlogger()
        time.sleep(2)
        first_name = ShippingInfo(self.driver)
        first_name.provide_first_name()
        last_name = ShippingInfo(self.driver)
        last_name.provide_last_name()
        address_line1 = ShippingInfo(self.driver)
        address_line1.provide_address1()
        address_line2 = ShippingInfo(self.driver)
        address_line2.provide_address2()
        city = ShippingInfo(self.driver)
        city.provide_city()
        select_state = ShippingInfo(self.driver)
        select_state.select_state()
        zip_input = ShippingInfo(self.driver)
        zip_input.provide_zip()
        phone_number = ShippingInfo(self.driver)
        phone_number.provide_phone_number()
        submit = ShippingInfo(self.driver)
        submit.submit()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Confirm Your Order | Aloe Care Health" in get_title)

    def test_place_order(self):
        log = self.getlogger()
        place_order = PlaceOrder(self.driver)
        place_order.place_order()
        get_title = self.driver.title
        log.info()
        assert ("Profile | Aloe Care Health" in get_title)

    def test_system_install_option1(self):
        log = self.getlogger()
        pop_up = InstallSystem(self.driver)
        pop_up.click_on_popup()
        option1 = InstallSystem(self.driver)
        option1.choose_option1()
        submit = InstallSystem(self.driver)
        submit.submit()
        get_title = self.driver.title
        log.info()
        assert ("Profile | Aloe Care Health" in get_title)

    def test_phone_number_ver(self):
        log = self.getlogger()
        phone = PhoneNumberVer(self.driver)
        phone.provide_phone_number()
        submit = PhoneNumberVer(self.driver)
        submit.submit()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Profile | Aloe Care Health" in get_title)

    def test_code_ver(self):
        log = self.getlogger()
        time.sleep(2)
        code = CodeVer(self.driver)
        code.provide_code(input("Your code? "))
        submit = CodeVer(self.driver)
        submit.submit()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Profile | Aloe Care Health" in get_title)

    def test_verify_your_info(self):
        log = self.getlogger()
        time.sleep(2)
        gender = VerifyYourInfo(self.driver)
        gender.choose_gender()
        submit = VerifyYourInfo(self.driver)
        submit.click_submit()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Profile | Aloe Care Health" in get_title)

    def test_add_cr_info(self):
        log = self.getlogger()
        first_name = AddCrInfo(self.driver)
        first_name.provide_first_name()
        last_name = AddCrInfo(self.driver)
        last_name.provide_last_name()
        phone = AddCrInfo(self.driver)
        phone.provide_phone()
        address1 = AddCrInfo(self.driver)
        address1.provide_address1()
        address2 = AddCrInfo(self.driver)
        address2.provide_address2()
        city = AddCrInfo(self.driver)
        city.provide_city()
        state = AddCrInfo(self.driver)
        state.select_state()
        zip_code = AddCrInfo(self.driver)
        zip_code.provide_zip()
        dob = AddCrInfo(self.driver)
        dob.select_dob()
        gender = AddCrInfo(self.driver)
        gender.choose_gender()
        relation = AddCrInfo(self.driver)
        relation.select_relation()
        lockbox = AddCrInfo(self.driver)
        lockbox.provide_lockbox_info()
        entry_inst = AddCrInfo(self.driver)
        entry_inst.provide_entry_instructions()
        submit = AddCrInfo(self.driver)
        submit.submit()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Setup Complete | Aloe Care Health" in get_title)

    def test_web_invite(self):
        log = self.getlogger()
        time.sleep(2)
        pop_up = WebInvite(self.driver)
        pop_up.tap_on()
        email_address = WebInvite(self.driver)
        email_address.provide_email_address()
        time.sleep(2)
        submit = WebInvite(self.driver)
        submit.send_invite()
        time.sleep(7)
        invite_sent_msg = self.driver.find_element(By.CSS_SELECTOR, "div[class='container alert-wrapper']").text
        log.info("Asserting Success Message in Invite Sent Banner")
        assert ("Invite sent" in invite_sent_msg)
