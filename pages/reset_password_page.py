from core.selectors import ResetPasswordPageSelectors


class ResetPasswordPage:
    @staticmethod
    def set_old_password(driver, old_password_value):
        driver.click(ResetPasswordPageSelectors.old_password)
        driver.set_value(ResetPasswordPageSelectors.old_password, old_password_value)
        driver.hide_keyboard()

    @staticmethod
    def set_new_password(driver, new_password_value):
        driver.click(ResetPasswordPageSelectors.new_password)
        driver.set_value(ResetPasswordPageSelectors.new_password, new_password_value)
        driver.hide_keyboard()

    @staticmethod
    def set_confirm_password(driver, confirm_password_value):
        driver.click(ResetPasswordPageSelectors.confirm_password)
        driver.set_value(ResetPasswordPageSelectors.confirm_password, confirm_password_value)
        driver.hide_keyboard()

    @staticmethod
    def click_reset_button(driver):
        driver.click(ResetPasswordPageSelectors.reset_button)

    @staticmethod
    def is_confirmation_message_displayed(driver):
        return driver.is_displayed(ResetPasswordPageSelectors.confirmation_message)

    @staticmethod
    def click_done(driver):
        driver.click(ResetPasswordPageSelectors.done_button)

    @staticmethod
    def click_proceed(driver):
        driver.click(ResetPasswordPageSelectors.proceed_button)
