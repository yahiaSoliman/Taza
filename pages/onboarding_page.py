import time

from core.selectors import OnBoardingSelectors


class OnBoardingPage:

    @staticmethod
    def click_next(driver):
        driver.click(OnBoardingSelectors.next)

    @staticmethod
    def click_skip(driver):
        driver.click(OnBoardingSelectors.skip)

    @staticmethod
    def click_lets_shop(driver):
        driver.click(OnBoardingSelectors.lets_shop)

    @staticmethod
    def skip_to_login(driver):

        if driver.is_device_ios():
            driver.tap_element(OnBoardingSelectors.skip_IOS)
            driver.click(OnBoardingSelectors.no_track_click_notification_IOS)
            driver.click(OnBoardingSelectors.enable_notification_IOS)
            driver.click(OnBoardingSelectors.allow_click_notification)

            # time.sleep(2)
            # driver.tap_element(OnBoardingSelectors.next)
            # time.sleep(2)
            # OnBoardingPage.click_lets_shop(driver)

        else:
            OnBoardingPage.click_next(driver)
            time.sleep(2)
            OnBoardingPage.click_next(driver)
            time.sleep(2)
            OnBoardingPage.click_lets_shop(driver)
