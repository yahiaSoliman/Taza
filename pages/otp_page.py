from core.selectors import OTPVerificationPageSelectors


class OTPPage:
    @staticmethod
    def find_not_your_number_button(driver):
        driver.find_element(OTPVerificationPageSelectors.not_your_number_button)

    @staticmethod
    def find_test_enter_code(driver):
        driver.find_element(OTPVerificationPageSelectors.text_enter_code)

    @staticmethod
    def register_set_otp(driver, otp_value):
        # driver.tap_element_with_relative_coordinate(OTPVerificationPageSelectors.otp_input, 20, 20)
        driver.tap_element_with_absolute_coordinates(135, 931)
        result = driver.driver.is_keyboard_shown()
        driver.assertTrue(result)
        for x in otp_value:
            driver.press_code(x)

    @staticmethod
    def forget_password_set_otp(driver, otp_value):
        # driver.tap_element_with_relative_coordinate(OTPVerificationPageSelectors.otp_input, 20, 20)
        driver.tap_element_with_absolute_coordinates(225, 966)
        result = driver.driver.is_keyboard_shown()
        driver.assertTrue(result)
        for x in otp_value:
            driver.press_code(x)
