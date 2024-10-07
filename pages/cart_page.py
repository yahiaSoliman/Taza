from core.selectors import CartPageSelectors, CheckOutPageSelectors, ReplaceMissingItems
from pages.order_page import ReceiptPage


class CartPage:
    @staticmethod
    def is_cart_page_title_displayed(driver):
        return driver.is_displayed(CartPageSelectors.cart_page_title)

    @staticmethod
    def is_cart_item_displayed(driver):
        return driver.is_displayed(CartPageSelectors.cart_item)

    @staticmethod
    def is_cart_empty(driver):
        return driver.is_displayed(CartPageSelectors.empty_cart_text)

    @staticmethod
    def click_clear_button(driver):
        driver.click(CartPageSelectors.clear_button)

    @staticmethod
    def click_checkout(driver):
        driver.click(CartPageSelectors.checkout_button)

    @staticmethod
    def click_minus_of_first_item(driver):
        driver.click(CartPageSelectors.minus_icon_first_element)

    @staticmethod
    def get_total_amount(driver):
        return driver.get_content_desc(CartPageSelectors.total_amount)

    @staticmethod
    def get_sub_total_amount(driver):
        return driver.get_content_desc(CartPageSelectors.sub_total)

    @staticmethod
    def get_delivery_charge(driver):
        txt = driver.get_content_desc(CartPageSelectors.delivery_charge)
        x = txt.split(" IQD")
        y = x[0].split(",")
        if len(y) > 1:
            delivery_charge = (int(y[0]) * 1000) + int(y[1])
        else:
            delivery_charge = int(y[0])
        return delivery_charge

    @staticmethod
    def get_total_amount_after_promo(driver):
        return driver.get_content_desc(CartPageSelectors.total_amount_after_promo_code)

    @staticmethod
    def get_subtotal_amount_before_promo(driver):
        return driver.get_content_desc(CartPageSelectors.subtotal_amount_before_promo_code)

    @staticmethod
    def get_subtotal_amount_after_promo(driver):
        return driver.get_content_desc(CartPageSelectors.subtotal_amount_after_promo_code)

    @staticmethod
    def click_plus_icon(driver):
        driver.click(CartPageSelectors.plus_icon)

    @staticmethod
    def get_number_of_cart_items(driver):
        return driver.get_number_of_elements(CartPageSelectors.cart_item)

    @staticmethod
    def get_list_of_cart_items(driver):
        return driver.get_list_of_elements(CartPageSelectors.cart_item)

    @staticmethod
    def get_item_description(driver):
        return driver.get_content_desc(CartPageSelectors.cart_item)

    @staticmethod
    def click_promo_code(driver):
        driver.click(CartPageSelectors.promo_code)

    @staticmethod
    def insert_promo_code(driver, code):
        driver.send_keys(CartPageSelectors.promo_code, code)

    @staticmethod
    def click_apply_promo(driver):
        driver.click(CartPageSelectors.apply_promo)

    @staticmethod
    def click_remove_promo(driver):
        driver.click(CartPageSelectors.remove_promo)

    @staticmethod
    def place_order(driver):
        CartPage.click_checkout(driver)
        result = CheckOutPage.is_checkout_page_title_displayed(driver)
        driver.assertTrue(result)  # verify checkout page is displayed
        CheckOutPage.click_place_order(driver)
        result = CheckOutPage.is_confirmation_message_displayed(driver)
        driver.assertTrue(result)  # verify confirmation message is displayed
        CheckOutPage.click_done_button(driver)
        result = ReceiptPage.is_order_id_displayed(driver)
        driver.assertTrue(result)  # verify order page is displayed


class CheckOutPage:

    @staticmethod
    def is_checkout_page_title_displayed(driver):
        return driver.is_displayed(CheckOutPageSelectors.checkout_page_title)

    @staticmethod
    def click_place_order(driver):
        driver.click(CheckOutPageSelectors.place_order_button)

    @staticmethod
    def is_confirmation_message_displayed(driver):
        return driver.is_displayed(CheckOutPageSelectors.confirmation_popup)

    @staticmethod
    def click_done_button(driver):
        driver.click(CheckOutPageSelectors.done_button)

    @staticmethod
    def click_change_button(driver):
        driver.click(CheckOutPageSelectors.selected_address_home)

    @staticmethod
    def select_work_address(driver):
        driver.click(CheckOutPageSelectors.work_address)

    @staticmethod
    def is_work_address_selected(driver):
        return driver.is_displayed(CheckOutPageSelectors.selected_address_work)

    @staticmethod
    def is_home_address_selected(driver):
        return driver.is_displayed(CheckOutPageSelectors.selected_address_home)

    @staticmethod
    def click_schedule_button(driver):
        driver.click(CheckOutPageSelectors.schedule_button)

    @staticmethod
    def click_schedule_order_button(driver):
        driver.click(CheckOutPageSelectors.schedule_order_button)

    @staticmethod
    def select_schedule_day(driver, day):
        driver.click(CheckOutPageSelectors.schedule_day(day))


class MissingItemsPage:

    @staticmethod
    def is_missing_items_message_displayed(driver):
        return driver.is_displayed(CartPageSelectors.missing_items_message)

    @staticmethod
    def click_view_and_replace(driver):
        return driver.click(CartPageSelectors.view_replace_button)

    @staticmethod
    def click_remove(driver):
        driver.click(ReplaceMissingItems.remove_btn)

    @staticmethod
    def click_replace_and_update(driver):
        driver.click(ReplaceMissingItems.replace_and_update_btn)

    @staticmethod
    def is_confirmation_message_displayed(driver):
        return driver.is_displayed(ReplaceMissingItems.confirmation_message)

    @staticmethod
    def is_new_total_amount_valid(driver):
        return driver.is_displayed(ReplaceMissingItems.new_total_amount)

    @staticmethod
    def click_place_order(driver):
        driver.click(ReplaceMissingItems.place_order_btn)

    @staticmethod
    def click_yahia_item_4_plus_icon(driver):
        driver.click(ReplaceMissingItems.yahia_item_04_plus_icon)

