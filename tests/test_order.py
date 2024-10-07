import calendar
import time
from datetime import date

from core.base_class import BaseClass
from core.data_sets import DataSets
from core.endPoints import EndPoints
from pages.cart_page import CartPage, CheckOutPage, MissingItemsPage
from pages.login_page import LoginPage
from pages.order_page import ReceiptPage
from pages.product_item_page import ProductItemPage
from pages.shop_page import ShopPage
from pages.side_menu_page import OrderHistoryPage


class OrderTests(BaseClass):
    """
    verify that user customer can cancel order
    placed order is listed in the history page
    customer can view details of item in history
    details of the item is valid
    """

    def test_cancel_order(self):
        """
        add one item to cart using endpoints
        """
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        access_token = response_login.json()['data']['access_token']

        response_clear_cart = EndPoints.clear_cart(access_token)
        assert response_clear_cart.status_code == 200

        response_update_cart = EndPoints.update_cart(access_token, DataSets.cart_object_1)
        assert response_update_cart.status_code == 200

        # place order
        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_address(self)
        ProductItemPage.click_view_basket(self)
        CartPage.place_order(self)

        # scroll to cancel order button
        time.sleep(5)
        e1 = ReceiptPage.find_missing_items_text_element(self)
        e2 = ReceiptPage.find_order_deliver_element(self)
        self.driver.scroll(e1, e2)
        time.sleep(3)
        ReceiptPage.click_cancel_order(self)

        # select reason of cancellation
        ReceiptPage.open_reason_list(self)
        ReceiptPage.select_reason(self)

        # confirm cancellation
        ReceiptPage.click_confirm_cancellation(self)
        ReceiptPage.click_done(self)
        ReceiptPage.is_cancelled_label_displayed(self)
        order_id = ReceiptPage.get_order_id(self)
        self.driver.back()
        # verify that user is redirected to order history current tab
        result = OrderHistoryPage.is_order_history_page_title_displayed(self)
        self.assertTrue(result)
        OrderHistoryPage.click_past_tab(self)
        result = OrderHistoryPage.is_past_order_displayed(self)
        self.assertTrue(result)  # verify that canceled order is displayed
        # verify that order id is existed in the list
        result = OrderHistoryPage.is_order_id_displayed_in_history_list(self, order_id)
        self.assertTrue(result)
        # verify that user can view the details of the order
        OrderHistoryPage.click_past_order_item(self)
        result = ReceiptPage.is_summary_title_displayed(self)
        self.assertTrue(result)
        # verify that details of the order is valid
        result = OrderHistoryPage.is_order_id_displayed_in_history_list(self, order_id)
        self.assertTrue(result)

    """
    verify that user customer can schedule order
    scheduled order is listed in the history page
    customer can view details of item in history
    details of the item is valid
    """

    def test_schedule_order(self):
        """
        add one item to cart using endpoints
        """
        response_login = EndPoints.login(DataSets.phoneSchedule, DataSets.password)
        access_token = response_login.json()['data']['access_token']

        response_clear_cart = EndPoints.clear_cart(access_token)
        assert response_clear_cart.status_code == 200

        response_update_cart = EndPoints.update_cart(access_token, DataSets.cart_object_1)
        assert response_update_cart.status_code == 200

        LoginPage.login(self, DataSets.phoneSchedule, DataSets.password)
        ProductItemPage.click_view_basket(self)
        CartPage.click_checkout(self)
        time.sleep(5)
        CheckOutPage.click_schedule_button(self)
        today_date = date.today()
        today_date_day = today_date.day
        x = calendar.month_name[today_date.month]
        CheckOutPage.select_schedule_day(self, x + " " + str(today_date_day + 1))
        CheckOutPage.click_schedule_order_button(self)
        CheckOutPage.click_place_order(self)
        result = CheckOutPage.is_confirmation_message_displayed(self)
        self.assertTrue(result)  # verify confirmation message is displayed
        CheckOutPage.click_done_button(self)
        result = ReceiptPage.is_order_id_displayed(self)
        self.assertTrue(result)  # verify order page is displayed
        result = ReceiptPage.is_scheduled_label_displayed(self)
        self.assertTrue(result)
        order_id = ReceiptPage.get_order_id(self)
        self.driver.back()
        # verify that user is redirected to order history current tab
        result = OrderHistoryPage.is_order_history_page_title_displayed(self)
        self.assertTrue(result)
        OrderHistoryPage.click_scheduled_tab(self)
        result = OrderHistoryPage.is_scheduled_order_displayed(self)
        self.assertTrue(result)  # verify that scheduled order is displayed
        # verify that order id is existed in the list
        result = OrderHistoryPage.is_order_id_displayed_in_history_list(self, order_id)
        self.assertTrue(result)
        # verify that user can view the details of the order
        OrderHistoryPage.click_scheduled_order_item(self)
        result = ReceiptPage.is_summary_title_displayed(self)
        self.assertTrue(result)
        # verify that details of the order is valid
        result = OrderHistoryPage.is_order_id_displayed_in_history_list(self, order_id)
        self.assertTrue(result)

        response_cancel_order = EndPoints.cancel_order(access_token, order_id.split("#")[1])
        assert response_cancel_order.status_code == 200

    """
    verify that user customer can place order
    placed order is listed in the history page
    customer can view details of item in history
    details of the item is valid
    """

    def test_place_order(self):
        """
         add one item to cart using endpoints
        """
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']

        response_clear_cart = EndPoints.clear_cart(access_token)
        self.assertEqual(response_clear_cart.status_code, 200, "clear cart endpoint fails")

        response_update_cart = EndPoints.update_cart(access_token, DataSets.cart_object_1)
        self.assertEqual(response_update_cart.status_code, 200, "update cart endpoint fails")

        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_home_address(self)
        ProductItemPage.click_view_basket(self)

        CartPage.place_order(self)
        order_id = ReceiptPage.get_order_id(self)
        self.driver.back()
        # verify that user is redirected to order history current tab
        result = OrderHistoryPage.is_order_history_page_title_displayed(self)
        self.assertTrue(result)
        # verify that order id is existed in the list
        result = OrderHistoryPage.is_order_id_displayed_in_history_list(self, order_id)
        self.assertTrue(result)
        # verify that user can view the details of the order
        OrderHistoryPage.click_placed_order_item(self)
        result = ReceiptPage.is_summary_title_displayed(self)
        self.assertTrue(result)
        # verify that details of the order is valid
        result = OrderHistoryPage.is_order_id_displayed_in_history_list(self, order_id)
        self.assertTrue(result)

    """
    verify that customer can modify the order after placing it.
    verify that the order id is still the same
    verify that the cart total is updated successfully
    """

    def test_modify_order(self):
        """
         add one item to cart using endpoints
        """
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']

        response_clear_cart = EndPoints.clear_cart(access_token)
        self.assertEqual(response_clear_cart.status_code, 200, "clear cart endpoint fails")

        response_update_cart = EndPoints.update_cart(access_token, DataSets.cart_object_1)
        self.assertEqual(response_update_cart.status_code, 200, "update cart endpoint fails")

        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_address(self)
        ProductItemPage.click_view_basket(self)
        CartPage.place_order(self)
        time.sleep(3)
        # scroll to modify order
        e1 = ReceiptPage.find_order_summary_title_element(self)
        e2 = ReceiptPage.find_order_deliver_element(self)
        self.driver.scroll(e1, e2)
        time.sleep(3)
        ReceiptPage.click_modify_order(self)
        ReceiptPage.click_update_order(self)
        result = CartPage.is_cart_page_title_displayed(self)

    """
    verify that user can't place order with missing items
    """

    def test_missing_items(self):
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']

        response_clear_cart = EndPoints.clear_cart(access_token)
        self.assertEqual(response_clear_cart.status_code, 200, "clear cart endpoint fails")

        response_update_cart = EndPoints.update_cart(access_token, DataSets.cart_object_2)
        self.assertEqual(response_update_cart.status_code, 200, "update cart endpoint fails")

        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_home_address(self)
        ProductItemPage.click_view_basket(self)

        sub_total_amount = CartPage.get_sub_total_amount(self)
        self.assertEqual("28,", sub_total_amount)
        CartPage.click_checkout(self)
        result = CheckOutPage.is_checkout_page_title_displayed(self)
        self.assertTrue(result)  # verify checkout page is displayed
        CheckOutPage.click_place_order(self)

        result = MissingItemsPage.is_missing_items_message_displayed(self)
        self.assertTrue(result)
        MissingItemsPage.click_view_and_replace(self)
        MissingItemsPage.click_remove(self)
        MissingItemsPage.click_yahia_item_4_plus_icon(self)

        MissingItemsPage.click_replace_and_update(self)
        result = MissingItemsPage.is_confirmation_message_displayed(self)
        self.assertTrue(result)
        self.assertTrue(result)
        MissingItemsPage.click_place_order(self)
        CheckOutPage.click_done_button(self)

        order_id = ReceiptPage.get_order_id(self)
        response_cancel_order = EndPoints.cancel_order(access_token, order_id.split("#")[1])
        self.assertEqual(response_cancel_order.status_code, 200, "cancel order endpoint fails")
