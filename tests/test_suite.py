import unittest

from HTMLTestRunner import HTMLTestRunner

from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from test_addresses import AddressesTest
from test_cart import CartTest
from test_favorites import FavoriteTest
from test_login import LoginTest
from test_order import OrderTests
from test_price import Price
from test_prodcut import ProductTests
from test_search import Search
from test_ui import ScreenTest
from test_account_settings import AccountChanges
from test_basket_popup import BasketPopup
from test_password import Passwords
from test_missing_items_request import TestMissingItemsRequests

suite_1 = unittest.TestSuite()
suite_1.addTest(LoginTest('test_login_logout'))
suite_1.addTest(LoginTest('test_register'))
suite_1.addTest(AddressesTest('test_add_address'))
suite_1.addTest(OrderTests('test_cancel_order'))
suite_1.addTest(OrderTests('test_place_order'))
suite_1.addTest(OrderTests('test_schedule_order'))
suite_1.addTest(OrderTests('test_modify_order'))
suite_1.addTest(FavoriteTest('test_add_remove_favorite'))
suite_1.addTest(AccountChanges('test_verify_validity_of_account_details_information'))
suite_1.addTest(AccountChanges('test_updating_account_first_name'))
suite_1.addTest(AccountChanges('test_updating_account_last_name'))
suite_1.addTest(AccountChanges('test_update_account_email'))
suite_1.addTest(AccountChanges('test_change_language'))
suite_1.addTest(BasketPopup('test_basket_total_price'))
suite_1.addTest(BasketPopup('test_basket_total_quantity'))
suite_1.addTest(CartTest('test_clear_cart'))
suite_1.addTest(CartTest('test_cart_total'))
suite_1.addTest(CartTest('test_delivery_address'))







if __name__ == '__main__':
    runner = HTMLTestRunner(title='yahia', open_in_browser=True)
    runner.run(suite_1)
