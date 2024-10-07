from core.base_class import BaseClass
from core.data_sets import DataSets
from core.endPoints import EndPoints
from pages.login_page import LoginPage
from pages.product_item_page import ProductItemPage
from pages.shop_page import ShopPage


class Price(BaseClass):
    def test_price_list(self):
        response_login = EndPoints.login(DataSets.phone_darkStore, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']
        response_clear_cart = EndPoints.clear_cart(access_token)
        self.assertEqual(response_clear_cart.status_code, 200, "clear cart endpoint fails")

        LoginPage.login(self, DataSets.phone_darkStore, DataSets.password)
        ShopPage.click_dora_address(self)
        ShopPage.search_for_item(self, DataSets.product_item_en)
        ShopPage.select_search_result(self)
        result = ProductItemPage.is_description_title_displayed(self)
        self.assertTrue(result)  # verify that item page is opened
        price = ProductItemPage.get_price(self)
        self.assertEqual(price, DataSets.lovita_dora_price)
        self.driver.back()
        self.hide_keyboard()
        self.driver.back()
        ShopPage.click_change_address(self)
        ShopPage.click_qhira_address(self)
        ShopPage.search_for_item(self, DataSets.product_item_en)
        ShopPage.select_search_result(self)
        result = ProductItemPage.is_description_title_displayed(self)
        self.assertTrue(result)  # verify that item page is opened
        price = ProductItemPage.get_price(self)
        self.assertEqual(price, DataSets.lovita_qhira_price)
