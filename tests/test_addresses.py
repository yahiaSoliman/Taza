import base64
import json
import time

from appium.webdriver.common.appiumby import AppiumBy

from core.base_class import BaseClass
from core.data_sets import DataSets
from core.endPoints import EndPoints
from pages.cart_page import CartPage, CheckOutPage
from pages.login_page import LoginPage
from pages.product_item_page import ProductItemPage
from pages.saved_addresses_page import SavedAddressesPage
from pages.shop_page import ShopPage
from pages.side_menu_page import SideMenuPage, SettingsPage


class AddressesTest(BaseClass):

    def test_add_address(self):
        phone_number = DataSets.generate_random_phone_number()

        register_response = EndPoints.register(phone_number, DataSets.password)

        self.driver.execute_script(
            'browserstack_executor: {"action": "annotate", "arguments": {"data":' +
            json.dumps(register_response.json()) +
            ',"level": "info"}}'
        )

        self.assertEqual(register_response.status_code, 200, "register endpoint fails")

        register_otp_response = EndPoints.register_otp(phone_number)
        self.assertEqual(register_otp_response.status_code, 200, "register otp endpoint fails")

        LoginPage.login(self, phone_number, DataSets.password)
        # open addresses page
        ShopPage.find_deliver_to_text(self)
        ShopPage.click_outside_address_box(self)
        ShopPage.click_burger_icon(self)

        file = open("./settings_icon.png", "rb")
        self.driver.find_element(AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8')).click()
        file.close()

        SettingsPage.click_saved_addresses(self)
        SavedAddressesPage.find_saved_addresses_page_title(self)

        self.add_address(DataSets.nickname_home)  # add home address

        result = SavedAddressesPage.is_nickname_displayed(self)
        self.assertTrue(result)

    def test_edit_address(self):
        # register new user
        phone_number = DataSets.generate_random_phone_number()
        register_response = EndPoints.register(phone_number, DataSets.password)
        self.assertEqual(register_response.status_code, 200, "register endpoint fails")
        register_otp_response = EndPoints.register_otp(phone_number)
        self.assertEqual(register_otp_response.status_code, 200, "register otp endpoint fails")
        # add address
        response_login = EndPoints.login(phone_number, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']
        response_add_address = EndPoints.add_address(access_token)
        self.assertEqual(response_add_address.status_code, 200, "add address endpoint fails")
        # login to mobile app
        LoginPage.login(self, phone_number, DataSets.password)
        # open settings
        ShopPage.click_burger_icon(self)
        """file = open("./settings_icon.png", "rb")
        self.driver.find_element(AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8')).click()
        file.close()"""
        self.driver.execute_script(
            'browserstack_executor: {"action": "annotate", "arguments": {"data":' +
            '"settings has been accessed"' +
            ',"level": "info"}}'
        )
        # open saved addresses
        SettingsPage.click_saved_addresses(self)
        SavedAddressesPage.find_saved_addresses_page_title(self)

        SavedAddressesPage.click_dots_icon(self)
        SavedAddressesPage.click_update(self)
        SavedAddressesPage.click_next(self)
        SavedAddressesPage.click_allow_gps_option(self)
        SavedAddressesPage.click_deliver_to(self)
        SavedAddressesPage.clear_nickname(self)
        SavedAddressesPage.set_nickname(self, DataSets.new_nickname)

        x = self.driver.current_package
        y = self.driver.current_activity()

        self.driver.hide_keyboard()
        SavedAddressesPage.click_update(self)
        time.sleep(5)
        self.driver.start_activity(x, y)
        result = SavedAddressesPage.is_new_nickname_displayed(self)  # verify that new nickname is displayed
        self.assertTrue(result)

    def test_delete_address(self):
        phone_number = DataSets.generate_random_phone_number()
        register_response = EndPoints.register(phone_number, DataSets.password)
        self.assertEqual(200, register_response.status_code, "register endpoint fails")

        register_otp_response = EndPoints.register_otp(phone_number)
        self.assertEqual(200, register_otp_response.status_code, "register otp endpoint fails")

        response_login = EndPoints.login(phone_number, DataSets.password)
        self.assertEqual(200, response_login.status_code, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']
        response_add_address = EndPoints.add_address(access_token)
        self.assertEqual(200, response_add_address.status_code, "add address endpoint fails")

        LoginPage.login(self, phone_number, DataSets.password)
        # open addresses page
        ShopPage.find_deliver_to_text(self)
        ShopPage.click_outside_address_box(self)
        ShopPage.click_burger_icon(self)

        file = open("./settings_icon.png", "rb")
        self.driver.find_element(AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8')).click()
        file.close()

        SettingsPage.click_saved_addresses(self)
        SavedAddressesPage.find_saved_addresses_page_title(self)

        SavedAddressesPage.click_dots_icon(self)
        SavedAddressesPage.click_delete(self)
        SavedAddressesPage.click_yes(self)
        result = SavedAddressesPage.is_not_found_text_displayed(self)
        self.assertTrue(result)

    def test_changing_default_address(self):
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']

        response_clear_cart = EndPoints.clear_cart(access_token)
        self.assertEqual(response_clear_cart.status_code, 200, "clear cart endpoint fails")

        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_home_address(self)
        ShopPage.search_for_item(self, DataSets.product_item_en)
        ShopPage.select_search_result(self)
        result = ProductItemPage.is_description_title_displayed(self)
        self.assertTrue(result)  # verify that item page is opened
        ProductItemPage.add_item_to_cart(self)
        CartPage.click_checkout(self)
        result = CheckOutPage.is_home_address_selected(self)
        self.assertTrue(result)  # verify that home address is selected
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()

        ShopPage.click_change_address(self)
        ShopPage.click_work_address(self)
        ProductItemPage.click_view_basket(self)
        CartPage.click_checkout(self)
        result = CheckOutPage.is_work_address_selected(self)
        self.assertTrue(result)  # verify that work address is selected

    def add_address(self, address_name):
        # set new address
        SavedAddressesPage.click_add_icon(self)
        SavedAddressesPage.click_next(self)
        SavedAddressesPage.click_allow_gps_option(self)
        time.sleep(5)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Not available")
        time.sleep(3)
        SavedAddressesPage.click_search_input(self)
        SavedAddressesPage.insert_search_value(self, DataSets.search_value)
        SavedAddressesPage.select_search_result(self)
        SavedAddressesPage.click_deliver_to(self)
        SavedAddressesPage.set_nickname(self, address_name)
        self.hide_keyboard()
        SavedAddressesPage.set_neighborhood(self, address_name)
        self.hide_keyboard()
        SavedAddressesPage.set_district(self, DataSets.district_value)
        self.hide_keyboard()
        SavedAddressesPage.click_save_address(self)
