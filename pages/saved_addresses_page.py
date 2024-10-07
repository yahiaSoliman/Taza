from core.selectors import SavedAddressesPageSelectors, NewAddressPageSelectors


class SavedAddressesPage:
    @staticmethod
    def click_add_icon(driver):
        driver.click(SavedAddressesPageSelectors.add_icon)

    @staticmethod
    def find_saved_addresses_page_title(driver):
        driver.find_element(SavedAddressesPageSelectors.saved_addresses_page_title)

    @staticmethod
    def is_nickname_displayed(driver):
        return driver.is_displayed(SavedAddressesPageSelectors.address_nickname)

    @staticmethod
    def is_new_nickname_displayed(driver):
        return driver.is_displayed(SavedAddressesPageSelectors.address_updated_nickname)

    @staticmethod
    def click_dots_icon(driver):
        # driver.tap_element_with_absolute_coordinates(950, 300) deprecated
        driver.click(SavedAddressesPageSelectors.dots_icon)

    @staticmethod
    def click_update(driver):
        driver.click(SavedAddressesPageSelectors.update_button)

    @staticmethod
    def click_delete(driver):
        driver.click(SavedAddressesPageSelectors.delete_button)

    @staticmethod
    def click_yes(driver):
        driver.click(SavedAddressesPageSelectors.yes_button)

    @staticmethod
    def is_not_found_text_displayed(driver):
        return driver.is_displayed(SavedAddressesPageSelectors.not_found_text)

    @staticmethod
    def click_next(driver):
        if driver.is_displayed(NewAddressPageSelectors.next_button):
            driver.tap_element_with_absolute_coordinates(500, 1500)

    @staticmethod
    def click_allow_gps_option(driver):
        if driver.is_displayed(NewAddressPageSelectors.allow_gps_button):
            driver.click(NewAddressPageSelectors.allow_gps_button)

    @staticmethod
    def click_search_input(driver):
        # driver.tap_element(NewAddressPageSelectors.search_input_field_inactive)
        driver.tap_element_with_absolute_coordinates(210, 100)

    @staticmethod
    def insert_search_value(driver, search_value):
        driver.set_value(NewAddressPageSelectors.search_input_field_active, search_value)

    @staticmethod
    def select_search_result(driver):
        driver.click(NewAddressPageSelectors.baghdad_mall_search_result)

    @staticmethod
    def click_deliver_to(driver):
        driver.click(NewAddressPageSelectors.deliver_to_button)

    @staticmethod
    def set_nickname(driver, nickname_value):
        driver.click(NewAddressPageSelectors.nick_name)
        driver.set_value(NewAddressPageSelectors.nick_name, nickname_value)

    @staticmethod
    def set_neighborhood(driver, neighbourhood_value):
        driver.click(NewAddressPageSelectors.neighbourhood)
        driver.set_value(NewAddressPageSelectors.neighbourhood, neighbourhood_value)

    @staticmethod
    def set_district(driver, district_value):
        driver.click(NewAddressPageSelectors.district)
        driver.set_value(NewAddressPageSelectors.district, district_value)

    @staticmethod
    def click_save_address(driver):
        driver.click(NewAddressPageSelectors.save_address)

    @staticmethod
    def clear_nickname(driver):
        driver.click(NewAddressPageSelectors.nick_name)
        driver.clear(NewAddressPageSelectors.nick_name)

    @staticmethod
    def click_save_updates(driver):
        driver.click(NewAddressPageSelectors.update_button)
