import time
from selenium.webdriver.common.by import By
from pageObjects.AddFamilyMemberFriendPage import FamilyMemberFriend
from pageObjects.BillingInfoPage import BillingInfo
from pageObjects.CreateYourAccountPage import CreateYourAccount
from pageObjects.EssentialsPlusBundlePage import EssentialsPlusPage
from pageObjects.HomePage import HomePage
from pageObjects.PlaceOrderPage import PlaceOrder
from pageObjects.ProductsPage import ProductsPage
from pageObjects.ReviewYourOrderPage import ReviewYourOrder
from pageObjects.ShippingInfoPage import ShippingInfo
from pageObjects.VerifyInfoServicePage import VerifyInfoService
from pageObjects.WebInvitePage import WebInvite
from pageObjects.WhereSystemPage import InstallSystem
from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_get_started(self):
        log = self.getlogger()
        get_started_with_order = HomePage(self.driver)
        get_started_with_order.get_started_risk_free()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Products | Aloe Care Health | Medical alert system for Seniors with options for fall detection" in get_title)

    def test_choose_product(self):
        log = self.getlogger()
        choose_essentialsplus = ProductsPage(self.driver)
        choose_essentialsplus.learn_more_essentialsplus()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Essentials Plus | Aloe Care Health: Medical Alert for Seniors, Caregivers. Fall detection options." in get_title)

    def test_essentialsplus_product(self):
        log = self.getlogger()
        essentials = EssentialsPlusPage(self.driver)
        essentials.essentialsplus_order()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Essentials Plus | Aloe Care Health: Medical Alert for Seniors, Caregivers. Fall detection options." in get_title)


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
        log.info("Asserting Page Title")
        assert ("Profile | Aloe Care Health" in get_title)

    def test_system_install_option2(self):
        log = self.getlogger()
        pop_up = InstallSystem(self.driver)
        pop_up.click_on_popup()
        option2 = InstallSystem(self.driver)
        option2.choose_option2()
        submit = InstallSystem(self.driver)
        submit.submit()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Profile | Aloe Care Health" in get_title)

    def test_acc_creation_fam_member_friend(self):
        log = self.getlogger()
        time.sleep(2)
        first_name = FamilyMemberFriend(self.driver)
        first_name.provide_first_name()
        last_name = FamilyMemberFriend(self.driver)
        last_name.provide_last_name()
        email = FamilyMemberFriend(self.driver)
        email.provide_email()
        phone = FamilyMemberFriend(self.driver)
        phone.provide_phone()
        relation = FamilyMemberFriend(self.driver)
        relation.select_relation()
        address1 = FamilyMemberFriend(self.driver)
        address1.provide_address1()
        address2 = FamilyMemberFriend(self.driver)
        address2.provide_address2()
        city = FamilyMemberFriend(self.driver)
        city.provide_city()
        state = FamilyMemberFriend(self.driver)
        state.select_state()
        zip_code = FamilyMemberFriend(self.driver)
        zip_code.provide_zip()
        gender = FamilyMemberFriend(self.driver)
        gender.choose_gender()
        submit = FamilyMemberFriend(self.driver)
        submit.submit()
        get_title = self.driver.title
        log.info("Asserting Page Title")
        assert ("Profile | Aloe Care Health" in get_title)

    def test_verify_info_service_address(self):
        log = self.getlogger()
        time.sleep(2)
        phone = VerifyInfoService(self.driver)
        phone.provide_phone()
        dob = VerifyInfoService(self.driver)
        dob.select_dob()
        gender = VerifyInfoService(self.driver)
        gender.choose_gender()
        lockbox = VerifyInfoService(self.driver)
        lockbox.provide_lockbox_info()
        entry_inst = VerifyInfoService(self.driver)
        entry_inst.provide_entry_instructions()
        submit = VerifyInfoService(self.driver)
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
