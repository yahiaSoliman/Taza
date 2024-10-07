from appium.webdriver.common.appiumby import AppiumBy

from core.base_class import BaseClass
from core.data_sets import DataSets
from pages.login_page import LoginPage
from pages.onboarding_page import OnBoardingPage
from pages.otp_page import OTPPage
from pages.shop_page import ShopPage
from pages.side_menu_page import SideMenuPage, SettingsPage, LanguagePage
from pages.sign_up_page import SignUpPage


class LoginTest(BaseClass):

    # T381 & T324
    def test_login_logout(self):
        LoginPage.login(self, DataSets.phone, DataSets.password)
        result = ShopPage.is_add_new_button_displayed(self)
        self.assertTrue(result)
        ShopPage.click_outside_address_box(self)
        ShopPage.click_burger_icon(self)
        SideMenuPage.click_user_name(self)
        SettingsPage.click_logout(self)
        result = LoginPage.is_sign_in_button_displayed(self)
        self.assertTrue(result)

    # T321
    def test_change_language(self):
        OnBoardingPage.skip_to_login(self)
        ShopPage.click_burger_icon(self)
        SideMenuPage.click_set_language(self)
        LanguagePage.click_arabic(self)
        LanguagePage.is_arabic_page_title_displayed(self)
        LanguagePage.click_english(self)
        LanguagePage.is_english_page_title_displayed(self)

    # T289
    def test_register(self):
        OnBoardingPage.skip_to_login(self)
        ShopPage.click_burger_icon(self)
        SideMenuPage.click_my_account(self)
        SettingsPage.click_signup(self)

        SignUpPage.set_first_name(self, DataSets.generate_random_name())
        SignUpPage.set_last_name(self, DataSets.generate_random_name())
        DataSets.register_phone = DataSets.generate_random_phone_number()
        SignUpPage.set_mobile_number(self, DataSets.register_phone)
        SignUpPage.set_password(self, DataSets.register_password)
        self.hide_keyboard()
        SignUpPage.click_next(self)
        OTPPage.find_test_enter_code(self)
        OTPPage.register_set_otp(self, DataSets.otp_key_codes)
        result = SettingsPage.is_logout_displayed(self)
        self.assertTrue(result)








