from appium.webdriver.common.appiumby import AppiumBy

from core.base_class import BaseClass
from core.data_sets import DataSets
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from pages.side_menu_page import SideMenuPage, LanguagePage


class Search(BaseClass):
    """
    verify that user can search for item with arabic language
    while the default language of the app is english
    """

    def test_search_arabic(self):
        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_home_address(self)
        ShopPage.search_for_item(self, DataSets.product_item_ar)
        result = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, 'Lovita Choco')]").is_displayed()
        self.assertTrue(result)

    """
    verify that user can search for item with english language 
    while the default language of the app is arabic
    """

    def test_search_english(self):
        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_home_address(self)
        ShopPage.click_burger_icon(self)
        SideMenuPage.click_set_language(self)
        LanguagePage.click_arabic(self)
        LanguagePage.is_arabic_page_title_displayed(self)
        LanguagePage.click_back(self)
        SideMenuPage.click_shop_ar(self)
        ShopPage.search_for_item(self, DataSets.product_item_en)
        result = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, 'لوفيتا تشوكو')]").is_displayed()
        self.assertTrue(result)
