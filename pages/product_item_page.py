from core.selectors import ProductItemPageSelectors
from pages.cart_page import CartPage


class ProductItemPage:

    @staticmethod
    def is_description_title_displayed(driver):
        return driver.is_displayed(ProductItemPageSelectors.description_title)

    @staticmethod
    def is_similar_products_title_displayed(driver):
        return driver.is_displayed(ProductItemPageSelectors.similar_products_title)

    @staticmethod
    def is_yahia_item_02_displayed(driver):
        return driver.is_displayed(ProductItemPageSelectors.yahia_item_02)

    @staticmethod
    def is_yahia_item_03_displayed(driver):
        return driver.is_displayed(ProductItemPageSelectors.yahia_item_03)

    @staticmethod
    def is_yahia_item_04_displayed(driver):
        return driver.is_displayed(ProductItemPageSelectors.yahia_item_04)

    @staticmethod
    def click_add_icon(driver):
        driver.click(ProductItemPageSelectors.add_icon)

    @staticmethod
    def click_add_icon_2(driver):
        driver.click(ProductItemPageSelectors.add_icon_2)

    @staticmethod
    def click_share_icon(driver):
        driver.click(ProductItemPageSelectors.share_icon)

    @staticmethod
    def click_view_basket(driver):
        driver.click(ProductItemPageSelectors.view_basket_button)

    @staticmethod
    def click_start_icon(driver):
        driver.click(ProductItemPageSelectors.star_icon)

    @staticmethod
    def get_basket_total(driver, price):
        if price == 2500:
            return driver.get_content_desc(ProductItemPageSelectors.basket_total_2500)
        elif price == 5000:
            return  driver.get_content_desc(ProductItemPageSelectors.basket_total_5000)

    @staticmethod
    def get_basket_quantity(driver, quantity):
        if quantity == 1:
            return driver.get_content_desc(ProductItemPageSelectors.basket_qt_1)
        elif quantity == 2:
            return driver.get_content_desc(ProductItemPageSelectors.basket_qt_2)

    @staticmethod
    def get_price(driver):
        return driver.get_content_desc(ProductItemPageSelectors.item_price)

    @staticmethod
    def is_cart_limit_warning_message_displayed(driver):
        return driver.is_displayed(ProductItemPageSelectors.cart_limit_warning_message)

    @staticmethod
    def add_item_to_cart(driver):
        ProductItemPage.click_add_icon(driver)
        ProductItemPage.click_view_basket(driver)
        result = CartPage.is_cart_page_title_displayed(driver)
        driver.assertTrue(result)  # verify that cart is opened
        result = CartPage.is_cart_item_displayed(driver)
        driver.assertTrue(result)  # verify that item is displayed in cart
