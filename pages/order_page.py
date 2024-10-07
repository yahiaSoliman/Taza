from core.selectors import ReceiptPageSelectors


class ReceiptPage:
    @staticmethod
    def is_order_id_displayed(driver):
        return driver.is_displayed(ReceiptPageSelectors.order_id)

    @staticmethod
    def get_order_id(driver):
        return driver.get_content_desc(ReceiptPageSelectors.order_id)

    @staticmethod
    def click_cancel_order(driver):
        driver.click(ReceiptPageSelectors.cancel_button)
        # driver.tap_element_with_absolute_coordinates(500, 2100)

    @staticmethod
    def find_order_summary_title_element(driver):
        return driver.find_element(ReceiptPageSelectors.order_summary_title)

    @staticmethod
    def find_order_deliver_element(driver):
        return driver.find_element(ReceiptPageSelectors.deliver_section_title)

    @staticmethod
    def find_missing_items_text_element(driver):
        return driver.find_element(ReceiptPageSelectors.text_of_missing_items)

    @staticmethod
    def is_summary_title_displayed(driver):
        return driver.is_displayed(ReceiptPageSelectors.order_summary_title)

    @staticmethod
    def find_shopping_bag_title(driver):
        return driver.find_element(ReceiptPageSelectors.shopping_bag_title)

    @staticmethod
    def click_confirm_cancellation(driver):
        driver.click(ReceiptPageSelectors.confirm_cancel_button)

    @staticmethod
    def click_done(driver):
        driver.click(ReceiptPageSelectors.done_button)

    @staticmethod
    def open_reason_list(driver):
        driver.click(ReceiptPageSelectors.reason_list)

    @staticmethod
    def select_reason(driver):
        driver.click(ReceiptPageSelectors.cancel_reason)

    @staticmethod
    def is_cancelled_label_displayed(driver):
        return driver.is_displayed(ReceiptPageSelectors.cancelled_label)

    @staticmethod
    def is_scheduled_label_displayed(driver):
        return driver.is_displayed(ReceiptPageSelectors.scheduled_label)

    @staticmethod
    def click_modify_order(driver):
        driver.click(ReceiptPageSelectors.modify_order)

    @staticmethod
    def click_update_order(driver):
        driver.click(ReceiptPageSelectors.update_order)

    @staticmethod
    def get_order_summary(driver):
        return driver.get_content_desc(ReceiptPageSelectors.order_summary_title)

    @staticmethod
    def click_suggest_missing_items(driver):
        driver.click(ReceiptPageSelectors.suggest_missing_items_button)


