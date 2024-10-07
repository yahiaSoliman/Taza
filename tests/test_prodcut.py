import base64
import time

from appium.webdriver.clipboard_content_type import ClipboardContentType
from appium.webdriver.common.appiumby import AppiumBy

from core.base_class import BaseClass
from core.data_sets import DataSets
from core.endPoints import EndPoints
from pages.login_page import LoginPage
from pages.product_item_page import ProductItemPage
from pages.shop_page import ShopPage


class ProductTests(BaseClass):

    def test_similar_products(self):
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']
        response_clear_cart = EndPoints.clear_cart(access_token)
        self.assertEqual(response_clear_cart.status_code, 200, "clear cart endpoint fails")

        # add item to cart
        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_address(self)
        ShopPage.search_for_item(self, DataSets.product_item_en_1)
        ShopPage.select_search_result(self)
        result = ProductItemPage.is_description_title_displayed(self)
        self.assertTrue(result)  # verify that item page is opened
        self.driver.swipe(50, 600, 50, 20, 500)

        result = ProductItemPage.is_similar_products_title_displayed(self)
        self.assertTrue(result)  # verify that similar products section is existed

        result = ProductItemPage.is_yahia_item_02_displayed(self)
        self.assertTrue(result)

        result = ProductItemPage.is_yahia_item_03_displayed(self)
        self.assertTrue(result)

        result = ProductItemPage.is_yahia_item_04_displayed(self)
        self.assertTrue(result)

    def test_share_product(self):
        # add item to cart
        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_address(self)
        ShopPage.search_for_item(self, DataSets.product_item_en)
        ShopPage.select_search_result(self)
        result = ProductItemPage.is_description_title_displayed(self)
        self.assertTrue(result)  # verify that item page is opened

        ProductItemPage.click_share_icon(self)
        time.sleep(10)
        """self.tap_element_with_absolute_coordinates(500, 2000)"""

        file = open("./copy_url.png", "rb")
        self.driver.find_element(AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8')).click()
        file.close()
        share_url = str(self.driver.get_clipboard(ClipboardContentType.PLAINTEXT))
        print(share_url)
        print(share_url[2:-1])
        self.driver.back()
        time.sleep(1)
        self.driver.get(share_url[2:-1])

        result = ProductItemPage.is_description_title_displayed(self)
        self.assertTrue(result)  # verify that item page is opened
