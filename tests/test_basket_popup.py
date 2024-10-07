import base64
import time

from appium.webdriver.common.appiumby import AppiumBy

from core.base_class import BaseClass
from core.data_sets import DataSets
from core.endPoints import EndPoints
from pages.login_page import LoginPage
from pages.product_item_page import ProductItemPage
from pages.shop_page import ShopPage, CategoryPage


class BasketPopup(BaseClass):
    """ test the validity of basket popup total price, and updating total price"""

    def test_basket_total_price(self):
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

        ProductItemPage.click_add_icon(self)
        time.sleep(3)
        self.assertEqual("2,500 IQD", ProductItemPage.get_basket_total(self, 2500))
        self.assertEqual("1", ProductItemPage.get_basket_quantity(self, 1))

        file = open("./plus_icon_new.png", "rb")
        self.driver.find_element(AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8')).click()
        file.close()

        time.sleep(3)
        self.assertEqual("5,000 IQD", ProductItemPage.get_basket_total(self, 5000))
        self.assertEqual("1", ProductItemPage.get_basket_quantity(self, 1))

    """
    verify update the total quantity of basket popup
    """

    def test_basket_total_quantity(self):
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']
        response_clear_cart = EndPoints.clear_cart(access_token)
        self.assertEqual(response_clear_cart.status_code, 200, "clear cart endpoint fails")

        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_home_address(self)

        CategoryPage.click_bath_category(self)
        time.sleep(3)

        ProductItemPage.click_add_icon(self)
        time.sleep(1)
        self.assertEqual("1", ProductItemPage.get_basket_quantity(self, 1))

        ProductItemPage.click_add_icon(self)
        time.sleep(1)
        self.assertEqual("2", ProductItemPage.get_basket_quantity(self, 2))
