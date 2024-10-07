import time

from pdf_gen.pdf_gen import pdf
from core.base_class import BaseClass
from core.data_sets import DataSets
from core.endPoints import EndPoints
from pages.cart_page import CartPage, CheckOutPage
from pages.login_page import LoginPage
from pages.onboarding_page import OnBoardingPage
from pages.product_item_page import ProductItemPage
from pages.shop_page import ShopPage, CategoryPage
from pages.side_menu_page import SideMenuPage, SettingsPage


class ScreenTest(BaseClass):

    def test_screen_shots(self):
        my_file = pdf("./", "UISreens")

        # clear cart
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']

        response_clear_cart = EndPoints.clear_cart(access_token)
        self.assertEqual(response_clear_cart.status_code, 200, "clear cart endpoint fails")

        # start UI
        OnBoardingPage.skip_to_login(self)
        ShopPage.click_burger_icon(self)
        SideMenuPage.click_my_account(self)
        SettingsPage.click_sign_in(self)
        time.sleep(3)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.write_text("Login Page", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        LoginPage.click_forget_password(self)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Forget Password", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        self.driver.back()
        LoginPage.click_create_account(self)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Register", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        self.driver.back()
        SettingsPage.click_sign_in(self)
        LoginPage.set_credentials_and_click_signin(self, DataSets.phone, DataSets.password)
        ShopPage.click_home_address(self)
        ShopPage.click_burger_icon(self)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Side Menu", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        SideMenuPage.click_user_name(self)
        SettingsPage.click_account_details(self)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("account details", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        self.driver.back()
        SettingsPage.click_saved_addresses(self)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Saved Addresses", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        self.driver.back()
        SettingsPage.click_reset_password(self)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Reset Password", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        self.driver.back()
        SettingsPage.click_notifications(self)
        time.sleep(3)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Notifications", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        self.driver.back()
        ShopPage.click_burger_icon(self)
        SideMenuPage.click_favorites(self)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Favorites", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        ShopPage.click_burger_icon(self)
        SideMenuPage.click_order_history(self)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("History", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        ShopPage.click_burger_icon(self)
        SideMenuPage.click_set_language(self)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("language page", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        """
        flow of placing order
        """
        self.driver.back()
        SideMenuPage.click_shop_en(self)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Shop Page", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        CategoryPage.click_beverages_category(self)
        time.sleep(2)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Category Page", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        CategoryPage.click_landessa_product(self)
        time.sleep(2)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Sub-Category Page", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        self.driver.back()
        time.sleep(1)
        self.driver.back()
        ShopPage.search_for_item(self, DataSets.product_item_en)
        ShopPage.select_search_result(self)
        result = ProductItemPage.is_description_title_displayed(self)
        self.assertTrue(result)  # verify that item page is opened
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Product Page", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        ProductItemPage.click_add_icon(self)
        ProductItemPage.click_view_basket(self)
        result = CartPage.is_cart_page_title_displayed(self)
        self.assertTrue(result)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Cart", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        CartPage.click_checkout(self)
        result = CheckOutPage.is_checkout_page_title_displayed(self)
        self.assertTrue(result)  # verify checkout page is displayed
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("Checkout", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        CheckOutPage.click_schedule_button(self)
        time.sleep(2)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("schedule", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        self.driver.back()
        CheckOutPage.click_place_order(self)
        result = CheckOutPage.is_confirmation_message_displayed(self)
        self.assertTrue(result)  # verify confirmation message is displayed
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("confirmation popup", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        CheckOutPage.click_done_button(self)
        time.sleep(3)
        self.driver.save_screenshot("UI_screenshot.png")
        my_file.next_page()
        my_file.write_text("receipt page", position="mid", x=250, y=800)
        my_file.insert_image("./UI_screenshot.png", 200, 200, 250, 550)

        my_file.save()
