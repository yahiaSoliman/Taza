from core.selectors import LoginPageSelectors
from pages.onboarding_page import OnBoardingPage
from pages.shop_page import ShopPage
from pages.side_menu_page import SideMenuPage, SettingsPage


class LoginPage:

    @staticmethod
    def click_mobile(driver):
        driver.click(LoginPageSelectors.mobile)

    @staticmethod
    def click_create_account(driver):
        driver.click(LoginPageSelectors.create_account_button)

    @staticmethod
    def set_mobile(driver, mobile_number):
        driver.click(LoginPageSelectors.mobile)
        driver.clear(LoginPageSelectors.mobile)
        driver.set_value(LoginPageSelectors.mobile, mobile_number)

    @staticmethod
    def set_password(driver, password_value):
        driver.click(LoginPageSelectors.password)
        driver.clear(LoginPageSelectors.password)
        driver.set_value(LoginPageSelectors.password, password_value)

    @staticmethod
    def click_sign_in_button(driver):
        driver.click(LoginPageSelectors.sign_in_button)

    @staticmethod
    def click_forget_password(driver):
        driver.click(LoginPageSelectors.forget_password)

    @staticmethod
    def is_wrong_credentials_error_displayed(driver):
        return driver.is_displayed(LoginPageSelectors.wrong_credentials_error_message)

    @staticmethod
    def set_credentials_and_click_signin(driver, phone_number, password_value):
        LoginPage.set_mobile(driver, phone_number)
        LoginPage.set_password(driver, password_value)

        if driver.is_device_ios():
            driver.tap_element_with_absolute_coordinates(100, 200)
        else:
            driver.hide_keyboard()

        LoginPage.click_sign_in_button(driver)

    @staticmethod
    def is_sign_in_button_displayed(driver):
        return driver.is_displayed(LoginPageSelectors.sign_in_button)

    @staticmethod
    def login(driver, username, password):
        OnBoardingPage.skip_to_login(driver)
        ShopPage.click_burger_icon(driver)
        SideMenuPage.click_my_account(driver)
        SettingsPage.click_sign_in(driver)
        LoginPage.set_credentials_and_click_signin(driver, username, password)

    @staticmethod
    def click_outside_to_hide_keyboard(driver):
        driver.tap_element_with_relative_coordinate(LoginPageSelectors.hide_keyboard, 150, 150)
