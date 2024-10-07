import time
from datetime import date

from core.base_class import BaseClass
from core.data_sets import DataSets
from core.endPoints import EndPoints
from pages.login_page import LoginPage
from pages.order_page import ReceiptPage
from pages.shop_page import ShopPage
from pages.side_menu_page import SideMenuPage, OrderHistoryPage


class TestMissingItemsRequests(BaseClass):

    # T381 & T324
    def test_suggest_missing_items_from_side_menu(self):
        LoginPage.login(self, DataSets.phone, DataSets.password)
        result = ShopPage.is_add_new_button_displayed(self)
        self.assertTrue(result)
        ShopPage.click_outside_address_box(self)
        ShopPage.click_burger_icon(self)
        SideMenuPage.click_missing_items(self)
        ShopPage.insert_missing_item_description_text(self, "test text")
        time.sleep(2)
        ShopPage.click_submit_missing_items(self)

    def test_suggest_missing_items_from_receipt(self):
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']

        create_order = EndPoints.create_order(access_token, str(date.today()))
        self.assertEqual(create_order.status_code, 200, "create order endpoint fails")

        # precondition for placing order by endpoints
        LoginPage.login(self, DataSets.phone, DataSets.password)
        result = ShopPage.is_add_new_button_displayed(self)
        self.assertTrue(result)
        ShopPage.click_outside_address_box(self)
        ShopPage.click_burger_icon(self)
        SideMenuPage.click_order_history(self)
        OrderHistoryPage.click_placed_order_item(self)
        time.sleep(2)

        # scroll to missing items suggestion button
        e1 = ReceiptPage.find_order_summary_title_element(self)
        e2 = ReceiptPage.find_order_deliver_element(self)
        self.driver.scroll(e1, e2)
        time.sleep(3)

        ReceiptPage.click_suggest_missing_items(self)
        ShopPage.insert_missing_item_description_text(self, "test text")
        time.sleep(2)
        ShopPage.click_submit_missing_items(self)