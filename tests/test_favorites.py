from core.base_class import BaseClass
from core.data_sets import DataSets
from core.endPoints import EndPoints
from pages.login_page import LoginPage
from pages.product_item_page import ProductItemPage
from pages.shop_page import ShopPage
from pages.side_menu_page import SideMenuPage, FavoritesPage


class FavoriteTest(BaseClass):

    # T298
    def test_add_remove_favorite(self):
        # validate that lovita product is not added to favorites
        response_login = EndPoints.login(DataSets.phone, DataSets.password)
        self.assertEqual(response_login.status_code, 200, "login endpoint fails")
        access_token = response_login.json()['data']['access_token']

        response_toggle = EndPoints.toggle_favorite_item(access_token)
        self.assertTrue(response_toggle.status_code == 200, "response toggle endpoint fails")
        if "added" in response_toggle.json()['data']:
            response_toggle = EndPoints.toggle_favorite_item(access_token)
        assert "removed" in response_toggle.json()['data']

        LoginPage.login(self, DataSets.phone, DataSets.password)
        ShopPage.click_address(self)
        # select item
        ShopPage.search_for_item(self, DataSets.product_item_en)
        ShopPage.select_search_result(self)
        result = ProductItemPage.is_description_title_displayed(self)
        self.assertTrue(result)  # verify that item page is opened
        # add to favorite
        ProductItemPage.click_start_icon(self)
        self.driver.back()
        self.hide_keyboard()
        self.driver.back()
        ShopPage.click_burger_icon(self)
        SideMenuPage.click_favorites(self)
        result = FavoritesPage.is_item_description_displayed(self)
        self.assertTrue(result, "item is not added to favorites")
        FavoritesPage.click_star_icon(self)
        result = FavoritesPage.is_favorites_empty(self)
        self.assertTrue(result, "item is not removed from the favorites")
