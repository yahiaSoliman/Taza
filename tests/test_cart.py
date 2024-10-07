import base64
import time

from appium.webdriver.common.appiumby import AppiumBy

from core.base_class import BaseClass
from core.data_sets import DataSets
from core.endPoints import EndPoints
from pages.cart_page import CartPage, CheckOutPage
from pages.login_page import LoginPage
from pages.product_item_page import ProductItemPage
from pages.shop_page import ShopPage, CategoryPage, ProductsPage


class CartTest(BaseClass):

    # login - open category - open product - add to cart - clear cart
    def test_clear_cart(self):
        # clear cart by endpoints
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']
        response_clear_cart = EndPoints.clear_cart(access_token)
        self.assertEqual(response_clear_cart.status_code, 200, "clear cart endpoint fails")
        # login to mobile app
        LoginPage.login(self, DataSets.phone, DataSets.password)
        # select address
        ShopPage.click_address(self)
        # open category
        CategoryPage.click_bath_category(self)
        time.sleep(3)
        ProductItemPage.add_item_to_cart(self)
        CartPage.click_clear_button(self)
        result = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Products").is_displayed()
        self.assertTrue(result)  # verify that item page is opened

    # T296
    # add to cart - search for item - verify cart total - increase item quantity - verify total is increased
    def test_cart_total(self):
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']
        response_clear_cart = EndPoints.clear_cart(access_token)
        self.assertEqual(response_clear_cart.status_code, 200, "clear cart endpoint fails")

        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_address(self)
        ShopPage.search_for_item(self, DataSets.product_item_en)
        ShopPage.select_search_result(self)
        result = ProductItemPage.is_description_title_displayed(self)
        self.assertTrue(result)  # verify that item page is opened
        ProductItemPage.add_item_to_cart(self)

        file = open("./cartPlusIcon.png", "rb")
        self.driver.find_element(AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8')).click()
        file.close()

        price_thousands_part = self.driver.find_element(AppiumBy.XPATH,
                                                        "//android.view.View[@content-desc='Sub-Total']/following-sibling::android.view.View").get_attribute(
            "content-desc")
        price_hundreds_part = self.driver.find_element(AppiumBy.XPATH,
                                                       "//android.view.View[@content-desc='Sub-Total']/following-sibling::android.view.View/following-sibling::android.view.View").get_attribute(
            "content-desc")

        sub_total = price_thousands_part + price_hundreds_part
        print(sub_total)
        self.assertEqual(sub_total, "5,000")

    def test_delivery_address(self):
        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_home_address(self)
        ShopPage.search_for_item(self, DataSets.product_item_en)
        ShopPage.select_search_result(self)
        result = ProductItemPage.is_description_title_displayed(self)
        self.assertTrue(result)  # verify that item page is opened
        ProductItemPage.add_item_to_cart(self)
        CartPage.click_checkout(self)
        CheckOutPage.click_change_button(self)
        CheckOutPage.select_work_address(self)
        CheckOutPage.is_work_address_selected(self)

    def test_add_remove_cart_item(self):
        # clear cart
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']
        response_clear_cart = EndPoints.clear_cart(access_token)
        self.assertEqual(response_clear_cart.status_code, 200, "clear cart endpoint fails")

        # add item to cart
        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_home_address(self)
        ShopPage.search_for_item(self, DataSets.product_item_en)
        ShopPage.select_search_result(self)
        result = ProductItemPage.is_description_title_displayed(self)
        self.assertTrue(result)  # verify that item page is opened
        ProductItemPage.add_item_to_cart(self)

        # remove the item from cart

        file = open("./deleteIcon.png", "rb")
        self.driver.find_element(AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8')).click()
        file.close()

        result = CartPage.is_cart_empty(self)
        self.assertTrue(result)

    """ verify that cart total is decreased by the promo-code amount
        verify that customer can remove the promo-code
    """

    def test_add_remove_promo_code(self):
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
        result = CheckOutPage.is_checkout_page_title_displayed(self)
        self.assertTrue(result)  # verify checkout page is displayed

        CartPage.click_promo_code(self)
        CartPage.insert_promo_code(self, DataSets.promo_code_1)
        CartPage.click_apply_promo(self)

        time.sleep(3)
        old_subtotal_amount = CartPage.get_subtotal_amount_before_promo(self)
        self.assertEqual(old_subtotal_amount, "2,500")
        new_subtotal_amount = str(CartPage.get_subtotal_amount_after_promo(self))
        self.assertTrue(new_subtotal_amount.__contains__("2,400"))

        CartPage.click_remove_promo(self)
        time.sleep(3)
        old_subtotal_amount = str(CartPage.get_subtotal_amount_before_promo(self))
        self.assertTrue(old_subtotal_amount.__contains__("2,500"))

    """
    verify that if the discount value is greater than the cart total
    the amount after discount will not be negative, instead it will be zero
    """

    def test_promo_code_maximum_discount(self):
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
        result = CheckOutPage.is_checkout_page_title_displayed(self)
        self.assertTrue(result)  # verify checkout page is displayed

        CartPage.click_promo_code(self)
        CartPage.insert_promo_code(self, DataSets.promo_code_2)
        CartPage.click_apply_promo(self)

        time.sleep(3)
        old_total_amount = str(CartPage.get_subtotal_amount_before_promo(self))
        self.assertTrue(old_total_amount.__contains__("2,500"))
        new_total_amount = CartPage.get_subtotal_amount_after_promo(self)
        self.assertEqual(new_total_amount, "IQD 0")

    """
    verify that the user can't place order with total cart amount
    less than 2000 IQD
    """

    def test_cart_limit(self):
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']

        response_clear_cart = EndPoints.clear_cart(access_token)
        self.assertEqual(response_clear_cart.status_code, 200, "clear cart endpoint fails")

        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_home_address(self)

        ShopPage.search_for_item(self, DataSets.product_item_en_1)
        ShopPage.select_search_result(self)
        result = ProductItemPage.is_description_title_displayed(self)
        self.assertTrue(result)  # verify that item page is opened

        ProductItemPage.click_add_icon(self)

        result = ProductItemPage.is_cart_limit_warning_message_displayed(self)
        self.assertTrue(result)
