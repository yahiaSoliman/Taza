import time

from core.selectors import ShopSelectors, TopPageSelectors, CategoryPageSelectors, ProductsPageSelectors


class ShopPage:
    @staticmethod
    def is_add_new_button_displayed(driver):
        return driver.is_displayed(ShopSelectors.add_new_address)

    @staticmethod
    def click_address(driver):
        ShopPage.find_deliver_to_text(driver)  # wait for address widget to be displayed
        driver.click(ShopSelectors.address)

    @staticmethod
    def click_work_address(driver):
        ShopPage.find_deliver_to_text(driver)  # wait for address widget to be displayed
        driver.click(ShopSelectors.work_address)

    @staticmethod
    def click_home_address(driver):
        driver.click(ShopSelectors.home_address)

    @staticmethod
    def click_dora_address(driver):
        ShopPage.find_deliver_to_text(driver)  # wait for address widget to be displayed
        driver.click(ShopSelectors.dora_address)

    @staticmethod
    def click_qhira_address(driver):
        ShopPage.find_deliver_to_text(driver)  # wait for address widget to be displayed
        driver.click(ShopSelectors.qhira_address)

    @staticmethod
    def click_change_address(driver):
        driver.click(TopPageSelectors.change_address_button)

    @staticmethod
    def click_food_category(driver):
        driver.click(ShopSelectors.food_category)

    @staticmethod
    def find_deliver_to_text(driver):
        if driver.is_element_displayed(ShopSelectors.deliver_to_text):
            driver.click(ShopSelectors.deliver_to_text)

    @staticmethod
    def click_outside_address_box(driver):
        driver.tap_element_with_relative_coordinate(ShopSelectors.outside_address_box, 100, 100)

    @staticmethod
    def click_burger_icon(driver):
        if driver.is_device_ios():
            time.sleep(20)
            driver.click(TopPageSelectors.burger_icon_IOS)
        else:
            driver.click(TopPageSelectors.burger_icon)

    @staticmethod
    def click_search_icon(driver):
        if driver.is_device_ios():
            driver.click(TopPageSelectors.search_icon_IOS)
        else:
            driver.click(TopPageSelectors.search_icon)

    @staticmethod
    def click_search_input_field(driver):
        driver.click(TopPageSelectors.search_input_field)

    @staticmethod
    def insert_search_text(driver, search_text):
        driver.set_value(TopPageSelectors.search_input_field, search_text)

    @staticmethod
    def select_search_result(driver):
        driver.click(TopPageSelectors.search_result_item)

    @staticmethod
    def search_for_item(driver, item_name):
        ShopPage.click_search_icon(driver)
        ShopPage.click_search_input_field(driver)
        ShopPage.insert_search_text(driver, item_name)
        driver.driver.hide_keyboard()

    @staticmethod
    def insert_missing_item_description_text(driver, text):
        driver.click(ShopSelectors.missing_items_input_field)
        driver.set_value(ShopSelectors.missing_items_input_field, text)

    @staticmethod
    def click_submit_missing_items(driver):
        driver.click(ShopSelectors.missing_items_submit_button)


class CategoryPage:
    @staticmethod
    def click_canned_foods_sub_category(driver):
        driver.click(CategoryPageSelectors.canned_foods_sub_category)

    @staticmethod
    def click_first_item_plus_icon(driver):
        driver.click(CategoryPageSelectors.first_item_plus_icon)

    @staticmethod
    def click_second_item_plus_icon(driver):
        driver.click(CategoryPageSelectors.second_item_plus_icon)

    @staticmethod
    def click_bath_category(driver):
        driver.click(CategoryPageSelectors.bath_supplies_category)

    @staticmethod
    def click_landessa_product(driver):
        driver.click(CategoryPageSelectors.landessa_product)


class ProductsPage:
    @staticmethod
    def click_on_item(driver):
        driver.click(ProductsPageSelectors.product_item)

    @staticmethod
    def click_sauce_filter(driver):
        driver.click(ProductsPageSelectors.sauce_filter)
