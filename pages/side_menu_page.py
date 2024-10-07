from core.selectors import SideMenuSelectors, FavoritesPageSelectors, SettingsSelectors, OrderHistoryPageSelectors, \
    LanguagePageSelectors


class SideMenuPage:

    @staticmethod
    def click_my_account(driver):
        driver.click(SideMenuSelectors.my_account)

    @staticmethod
    def click_shop_ar(driver):
        driver.click(SideMenuSelectors.shop_ar)

    @staticmethod
    def click_shop_en(driver):
        driver.click(SideMenuSelectors.shop_en)

    @staticmethod
    def click_set_language(driver):
        driver.click(SideMenuSelectors.set_language)

    @staticmethod
    def click_user_name(driver):
        driver.click(SideMenuSelectors.user_name_yahia)

    @staticmethod
    def click_user_name_ozgur(driver):
        driver.click(SideMenuSelectors.user_name_ozgur)

    @staticmethod
    def click_order_history(driver):
        driver.click(SideMenuSelectors.order_history)

    @staticmethod
    def click_favorites(driver):
        driver.click(SideMenuSelectors.favorites)

    @staticmethod
    def click_missing_items(driver):
        driver.click(SideMenuSelectors.missing_items)


class FavoritesPage:
    @staticmethod
    def is_item_description_displayed(driver):
        return driver.is_displayed(FavoritesPageSelectors.item_description)

    @staticmethod
    def is_favorites_empty(driver):
        return driver.is_displayed(FavoritesPageSelectors.no_favorites_text)

    @staticmethod
    def click_star_icon(driver):
        driver.click(FavoritesPageSelectors.star_icon)


class SettingsPage:
    @staticmethod
    def click_sign_in(driver):
        driver.click(SettingsSelectors.sign_in)

    @staticmethod
    def click_account_details(driver):
        driver.click(SettingsSelectors.account_details)

    @staticmethod
    def click_signup(driver):
        driver.click(SettingsSelectors.sign_up)

    @staticmethod
    def is_logout_displayed(driver):
        return driver.is_displayed(SettingsSelectors.logout)

    @staticmethod
    def click_logout(driver):
        driver.click(SettingsSelectors.logout)

    @staticmethod
    def click_saved_addresses(driver):
        driver.click(SettingsSelectors.saved_addresses)

    @staticmethod
    def click_reset_password(driver):
        driver.click(SettingsSelectors.reset_password)

    @staticmethod
    def click_notifications(driver):
        driver.click(SettingsSelectors.notifications)


class OrderHistoryPage:
    @staticmethod
    def is_placed_order_displayed(driver):
        return driver.is_displayed(OrderHistoryPageSelectors.current_order_item)

    @staticmethod
    def is_order_id_displayed_in_history_list(driver, order_id):
        return driver.is_displayed(OrderHistoryPageSelectors.placed_order_with_certain_id(order_id))

    @staticmethod
    def is_past_order_displayed(driver):
        return driver.is_displayed(OrderHistoryPageSelectors.past_order_item)

    @staticmethod
    def click_past_tab(driver):
        driver.click(OrderHistoryPageSelectors.past_tab)

    @staticmethod
    def click_scheduled_tab(driver):
        driver.click(OrderHistoryPageSelectors.scheduled_tab)

    @staticmethod
    def click_scheduled_order_item(driver):
        driver.click(OrderHistoryPageSelectors.scheduled_order_item)

    @staticmethod
    def click_placed_order_item(driver):
        driver.click(OrderHistoryPageSelectors.current_order_item)

    @staticmethod
    def click_past_order_item(driver):
        driver.click(OrderHistoryPageSelectors.past_order_item)

    @staticmethod
    def is_scheduled_order_displayed(driver):
        return driver.is_displayed(OrderHistoryPageSelectors.scheduled_order_item)

    @staticmethod
    def is_order_history_page_title_displayed(driver):
        return driver.is_displayed(OrderHistoryPageSelectors.history_page_title)


class LanguagePage:
    @staticmethod
    def click_arabic(driver):
        driver.click(LanguagePageSelectors.arabic)

    @staticmethod
    def click_english(driver):
        driver.click(LanguagePageSelectors.english)

    @staticmethod
    def is_arabic_page_title_displayed(driver):
        return driver.is_displayed(LanguagePageSelectors.page_title_arabic)

    @staticmethod
    def is_english_page_title_displayed(driver):
        return driver.is_displayed(LanguagePageSelectors.page_title_english)

    @staticmethod
    def click_back(driver):
        driver.click(LanguagePageSelectors.back_button)
