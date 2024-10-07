from core.selectors import ForgetPasswordPageSelectors, CreateNewPasswordPageSelectors


class ForgetPasswordPage:
    @staticmethod
    def set_mobile_no(driver, mobile_number):
        driver.click(ForgetPasswordPageSelectors.mobile_no)
        driver.set_value(ForgetPasswordPageSelectors.mobile_no, mobile_number)

    @staticmethod
    def click_send_button(driver):
        driver.click(ForgetPasswordPageSelectors.send_button)


class CreateNewPasswordPage:
    @staticmethod
    def set_new_password(driver, new_password_value):
        driver.click(CreateNewPasswordPageSelectors.new_password)
        driver.set_value(CreateNewPasswordPageSelectors.new_password, new_password_value)

    @staticmethod
    def set_confirm_password(driver, confirm_password_value):
        driver.click(CreateNewPasswordPageSelectors.confirm_password)
        driver.set_value(CreateNewPasswordPageSelectors.confirm_password, confirm_password_value)

    @staticmethod
    def click_reset_button(driver):
        driver.click(CreateNewPasswordPageSelectors.reset_button)

    @staticmethod
    def is_confirmation_message_displayed(driver):
        return driver.is_displayed(CreateNewPasswordPageSelectors.confirmation_message)

    @staticmethod
    def click_sign_in(driver):
        driver.click(CreateNewPasswordPageSelectors.sign_in_button)
