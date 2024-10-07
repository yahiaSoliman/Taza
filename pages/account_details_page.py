from core.selectors import AccountDetailsPageSelectors
from core.data_sets import DataSets


class AccountDetailsPage:
    @staticmethod
    def click_delete_account_button(driver):
        driver.click(AccountDetailsPageSelectors.delete_Account_button)

    @staticmethod
    def click_confirm_delete_button(driver):
        driver.click(AccountDetailsPageSelectors.confirm_delete_button)

    @staticmethod
    def click_ok_button(driver):
        driver.click(AccountDetailsPageSelectors.OK_button)

    @staticmethod
    def is_confirmation_message_displayed(driver):
        return driver.is_displayed(AccountDetailsPageSelectors.confirmation_message)

    @staticmethod
    def update_password(driver):
        driver.click(AccountDetailsPageSelectors.first_address)
        driver.click(AccountDetailsPageSelectors.update_address)
        driver.click(AccountDetailsPageSelectors.click_next)

    @staticmethod
    def update_account_firstname(driver, name):
        driver.click(AccountDetailsPageSelectors.first_name)
        driver.clear(AccountDetailsPageSelectors.first_name)
        driver.set_value(AccountDetailsPageSelectors.first_name, name)

    @staticmethod
    def update_account_lastname(driver, name):
        driver.click(AccountDetailsPageSelectors.last_name)
        driver.clear(AccountDetailsPageSelectors.last_name)
        driver.set_value(AccountDetailsPageSelectors.last_name, name)

    @staticmethod
    def update_account_email(driver, email):
        driver.click(AccountDetailsPageSelectors.account_email)
        driver.clear(AccountDetailsPageSelectors.account_email)
        driver.set_value(AccountDetailsPageSelectors.account_email, email)

    @staticmethod
    def verify_display_account_details(driver):
        assert DataSets.last_name in driver.get_text(AccountDetailsPageSelectors.last_name)
        assert DataSets.first_name in driver.get_text(AccountDetailsPageSelectors.first_name)
        assert DataSets.email in driver.get_text(AccountDetailsPageSelectors.account_email)

    @staticmethod
    def click_save(driver):
        driver.click(AccountDetailsPageSelectors.account_save)

    @staticmethod
    def get_lastname_text(driver):
        return driver.get_text(AccountDetailsPageSelectors.last_name)

    @staticmethod
    def get_firstname_text(driver):
        return driver.get_text(AccountDetailsPageSelectors.first_name)

    @staticmethod
    def get_email_text(driver):
        return driver.get_text(AccountDetailsPageSelectors.account_email)
