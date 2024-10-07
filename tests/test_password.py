import base64

from appium.webdriver.common.appiumby import AppiumBy

from core.base_class import BaseClass
from core.data_sets import DataSets
from core.endPoints import EndPoints
from pages.login_page import LoginPage
from pages.onboarding_page import OnBoardingPage
from pages.otp_page import OTPPage
from pages.forget_password_page import ForgetPasswordPage, CreateNewPasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages.shop_page import ShopPage
from pages.side_menu_page import SideMenuPage, SettingsPage


class Passwords(BaseClass):

    # T319
    def test_forget_password(self):
        phone_number = DataSets.generate_random_phone_number()

        register_response = EndPoints.register(phone_number, DataSets.password)
        print(register_response.json())
        self.assertEqual(register_response.status_code, 200, "register endpoint fails")
        register_otp_response = EndPoints.register_otp(phone_number)
        self.assertEqual(register_otp_response.status_code, 200, "register otp endpoint fails")

        OnBoardingPage.skip_to_login(self)
        ShopPage.click_burger_icon(self)
        SideMenuPage.click_my_account(self)
        SettingsPage.click_sign_in(self)
        LoginPage.click_forget_password(self)
        ForgetPasswordPage.set_mobile_no(self, phone_number)
        self.hide_keyboard()
        ForgetPasswordPage.click_send_button(self)
        OTPPage.find_not_your_number_button(self)
        OTPPage.forget_password_set_otp(self, DataSets.otp_key_codes)
        CreateNewPasswordPage.set_new_password(self, DataSets.new_password)
        self.hide_keyboard()
        CreateNewPasswordPage.set_confirm_password(self, DataSets.new_password)
        self.driver.hide_keyboard()
        CreateNewPasswordPage.click_reset_button(self)
        result = CreateNewPasswordPage.is_confirmation_message_displayed(self)
        self.assertTrue(result)  # verify that user new password set successfully

        # validate login with old and new password
        response = EndPoints.login(phone_number, DataSets.password)
        self.assertNotEqual(response.status_code, 200)
        response = EndPoints.login(phone_number, DataSets.new_password)
        self.assertEqual(response.status_code, 200)

    # T319
    def test_reset_password(self):
        phone_number = DataSets.generate_random_phone_number()

        register_response = EndPoints.register(phone_number, DataSets.password)
        self.assertEqual(register_response.status_code, 200, "register endpoint fails")
        register_otp_response = EndPoints.register_otp(phone_number)
        self.assertEqual(register_otp_response.status_code, 200, "register otp endpoint fails")

        LoginPage.login(self, phone_number, DataSets.password)
        ShopPage.find_deliver_to_text(self)
        ShopPage.click_outside_address_box(self)
        ShopPage.click_burger_icon(self)

        file = open("./settings_icon.png", "rb")
        self.driver.find_element(AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8')).click()
        file.close()

        SettingsPage.click_reset_password(self)
        ResetPasswordPage.set_old_password(self, DataSets.password)
        ResetPasswordPage.set_new_password(self, DataSets.new_password)
        ResetPasswordPage.set_confirm_password(self, DataSets.new_password)
        ResetPasswordPage.click_reset_button(self)
        ResetPasswordPage.click_proceed(self)
        # validate
        result = ResetPasswordPage.is_confirmation_message_displayed(self)
        self.assertTrue(result)
        ResetPasswordPage.click_done(self)

        # validate login with old and new password
        response = EndPoints.login(phone_number, DataSets.password)
        self.assertNotEqual(response.status_code, 200)
        response = EndPoints.login(phone_number, DataSets.new_password)
        self.assertEqual(response.status_code, 200)
