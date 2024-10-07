from core.selectors import SignUpPageSelectors


class SignUpPage:
    @staticmethod
    def set_first_name(driver, first_name_value):
        driver.click(SignUpPageSelectors.first_name_input_field)
        driver.set_value(SignUpPageSelectors.first_name_input_field, first_name_value)

    @staticmethod
    def set_last_name(driver, last_name_value):
        driver.click(SignUpPageSelectors.last_name_input_field)
        driver.set_value(SignUpPageSelectors.last_name_input_field, last_name_value)

    @staticmethod
    def set_mobile_number(driver, mobile_number):
        driver.click(SignUpPageSelectors.mobile_no_input_field)
        driver.set_value(SignUpPageSelectors.mobile_no_input_field, mobile_number)

    @staticmethod
    def set_password(driver, password_value):
        driver.click(SignUpPageSelectors.password_input_field)
        driver.set_value(SignUpPageSelectors.password_input_field, password_value)

    @staticmethod
    def click_next(driver):
        driver.click(SignUpPageSelectors.next_button)
