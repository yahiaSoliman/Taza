import base64

from appium.webdriver.common.appiumby import AppiumBy

from core.base_class import BaseClass
from core.data_sets import DataSets
from core.endPoints import EndPoints
from core.selectors import AccountDetailsPageSelectors
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from pages.side_menu_page import SideMenuPage, SettingsPage
from pages.account_details_page import AccountDetailsPage


class AccountChanges(BaseClass):

    def test_verify_validity_of_account_details_information(self):
        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.find_deliver_to_text(self)
        ShopPage.click_outside_address_box(self)
        ShopPage.click_burger_icon(self)
        SideMenuPage.click_user_name(self)
        SettingsPage.click_account_details(self)
        AccountDetailsPage.verify_display_account_details(self)

    def test_updating_account_first_name(self):
        name = DataSets.generate_random_name()
        # verify that user can change his name
        LoginPage.login(self, DataSets.phone_for_account_update, DataSets.password_for_account_update)
        ShopPage.find_deliver_to_text(self)
        ShopPage.click_outside_address_box(self)
        ShopPage.click_burger_icon(self)

        file = open("./settings_icon.png", "rb")
        self.driver.find_element(AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8')).click()
        file.close()

        SettingsPage.click_account_details(self)

        AccountDetailsPage.update_account_firstname(self, name)
        self.driver.press_keycode(66)
        AccountDetailsPage.click_save(self)
        self.wait_for_element_visible(AccountDetailsPageSelectors.first_name)
        self.driver.back()
        SettingsPage.click_account_details(self)
        updated_firstname_value = AccountDetailsPage.get_firstname_text(self)
        assert name in updated_firstname_value

    def test_updating_account_last_name(self):
        name = DataSets.generate_random_name()
        # verify that user can change his name
        LoginPage.login(self, DataSets.phone_for_account_update, DataSets.password_for_account_update)
        ShopPage.find_deliver_to_text(self)
        ShopPage.click_outside_address_box(self)
        ShopPage.click_burger_icon(self)

        file = open("./settings_icon.png", "rb")
        self.driver.find_element(AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8')).click()
        file.close()

        SettingsPage.click_account_details(self)
        AccountDetailsPage.update_account_lastname(self, name)
        self.driver.press_keycode(66)
        AccountDetailsPage.click_save(self)
        self.wait_for_element_visible(AccountDetailsPageSelectors.last_name)
        self.driver.back()
        SettingsPage.click_account_details(self)
        updated_lastname_value = AccountDetailsPage.get_lastname_text(self)
        assert name in updated_lastname_value

    def test_update_account_email(self):
        email = DataSets.generate_random_email()
        # verify that user can change his email
        LoginPage.login(self, DataSets.phone_for_account_update, DataSets.password_for_account_update)
        ShopPage.find_deliver_to_text(self)
        ShopPage.click_outside_address_box(self)
        ShopPage.click_burger_icon(self)

        file = open("./settings_icon.png", "rb")
        self.driver.find_element(AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8')).click()
        file.close()

        SettingsPage.click_account_details(self)

        AccountDetailsPage.update_account_email(self, email)
        self.driver.press_keycode(66)
        AccountDetailsPage.click_save(self)
        self.wait_for_element_visible(AccountDetailsPageSelectors.account_email)
        self.driver.back()
        SettingsPage.click_account_details(self)
        updated_email_value = AccountDetailsPage.get_email_text(self)
        assert email in updated_email_value

    def test_remove_account(self):
        phone_number = DataSets.generate_random_phone_number()

        register_response = EndPoints.register(phone_number, DataSets.password)
        self.assertEqual(register_response.status_code, 200, "register endpoint fails")
        register_otp_response = EndPoints.register_otp(phone_number)
        self.assertEqual(register_otp_response.status_code, 200, "register otp endpoint fails")

        LoginPage.login(self, phone_number, DataSets.register_password)
        ShopPage.find_deliver_to_text(self)
        ShopPage.click_outside_address_box(self)
        ShopPage.click_burger_icon(self)
        SideMenuPage.click_user_name(self)
        SettingsPage.click_account_details(self)
        AccountDetailsPage.click_delete_account_button(self)
        AccountDetailsPage.click_confirm_delete_button(self)

        # validate login with old and new password
        response = EndPoints.login(phone_number, DataSets.password)
        self.assertNotEqual(response.status_code, 200)

