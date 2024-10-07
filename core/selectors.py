import base64

from appium.webdriver.common.appiumby import AppiumBy

from core.data_sets import DataSets


class OnBoardingSelectors:
    next = (AppiumBy.ACCESSIBILITY_ID, "NEXT")
    lets_shop = (AppiumBy.ACCESSIBILITY_ID, "LET'S SHOP!")
    enable_notification_IOS = (AppiumBy.NAME, "Enable notifications")
    allow_click_notification = (AppiumBy.NAME, "Allow")
    no_track_click_notification_IOS = (AppiumBy.NAME, "Ask App Not to Track")
    text_affordable = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Affordable')]")
    text_affordable_IOS = (AppiumBy.XPATH, "//*[contains(@name, 'Affordable')]")
    skip = (AppiumBy.ACCESSIBILITY_ID, "Skip intro")
    skip_IOS = (AppiumBy.IOS_PREDICATE, "label == 'Skip intro'")


class TopPageSelectors:
    burger_icon = (AppiumBy.XPATH, "//android.widget.Button")
    burger_icon_IOS = (AppiumBy.XPATH, "(//XCUIElementTypeButton)[1]")
    search_icon = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    search_icon_IOS = (AppiumBy.XPATH, "(//XCUIElementTypeButton)[2]")
    search_input_field = (AppiumBy.XPATH, "(//android.widget.ImageView)[2]")
    search_result_item = (AppiumBy.XPATH, "(//*[contains(@content-desc,'IQD')])[1]")
    change_address_button = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Delivering')]")


class SideMenuSelectors:
    my_account = (AppiumBy.XPATH, "//*[@*[contains(.,'My Account')]]")
    set_language = (AppiumBy.ACCESSIBILITY_ID, "Set Language To")
    user_name_yahia = (AppiumBy.XPATH, "//*[@*[contains(.,'yahia')]]")
    user_name_ozgur = (AppiumBy.XPATH, "//*[@*[contains(.,'ozgurY')]]")
    order_history = (AppiumBy.ACCESSIBILITY_ID, "Order History")
    favorites = (AppiumBy.ACCESSIBILITY_ID, "Favourites")
    shop_ar = (AppiumBy.ACCESSIBILITY_ID, "تسوق")
    shop_en = (AppiumBy.ACCESSIBILITY_ID, "Shop")
    missing_items = (AppiumBy.ACCESSIBILITY_ID, "Missing Items")


class SettingsSelectors:
    sign_in = (AppiumBy.ACCESSIBILITY_ID, "Sign In")
    account_details = (AppiumBy.XPATH,
                       "(//*[contains(@content-desc,'Account details')])[2] | (//XCUIElementTypeStaticText[@name='Account details'])[2]")
    sign_up = (AppiumBy.XPATH, "//android.widget.Button[contains(@content-desc,'Sign Up')]")
    logout = (AppiumBy.ACCESSIBILITY_ID, "Log out")
    saved_addresses = (AppiumBy.ACCESSIBILITY_ID, "Saved Addresses")
    reset_password = (AppiumBy.ACCESSIBILITY_ID, "Reset Password")
    notifications = (AppiumBy.ACCESSIBILITY_ID, "Notifications")


class LoginPageSelectors:
    mobile = (AppiumBy.XPATH, "//android.widget.EditText[1] | //*[@*[contains(.,'Mobile')]]")
    password = (AppiumBy.XPATH, "//android.widget.EditText[2] | //*[@*[contains(.,'Password')]]")
    hide_keyboard = (AppiumBy.CLASS_NAME, "XCUIElementTypeImage")
    sign_in_button = (AppiumBy.ACCESSIBILITY_ID, "Sign In")
    forget_password = (AppiumBy.XPATH, "//android.widget.Button[contains(@content-desc,'Forgot password')]")
    wrong_credentials_error_message = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'Please use "
                                                       "valid credentials')]")
    create_account_button = (AppiumBy.ACCESSIBILITY_ID, "Create an account")


class ForgetPasswordPageSelectors:
    mobile_no = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    send_button = (AppiumBy.ACCESSIBILITY_ID, "Send instructions")


class ResetPasswordPageSelectors:
    old_password = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
    new_password = (AppiumBy.XPATH, "(//android.widget.EditText)[2]")
    confirm_password = (AppiumBy.XPATH, "(//android.widget.EditText)[3]")
    reset_button = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Reset Password']")
    proceed_button = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='PROCEED']")
    confirmation_message = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'Password changed "
                                            "successfully')]")
    done_button = (AppiumBy.ACCESSIBILITY_ID, "Done")


class OTPVerificationPageSelectors:
    otp_input = (AppiumBy.XPATH, "//android.view.View[@clickable='true']")
    not_your_number_button = (AppiumBy.XPATH, "//android.widget.Button[contains(@content-desc,'Not your number')]")
    text_enter_code = (AppiumBy.ACCESSIBILITY_ID, "Enter the code from the SMS sent to")


class CreateNewPasswordPageSelectors:
    new_password = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
    confirm_password = (AppiumBy.XPATH, "(//android.widget.EditText)[2]")
    reset_button = (AppiumBy.ACCESSIBILITY_ID, "Reset Password")
    confirmation_message = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'Password Reset "
                                            "Successfully')]")
    sign_in_button = (AppiumBy.ACCESSIBILITY_ID, "Sign In")


class ShopSelectors:
    deliver_address = (AppiumBy.ACCESSIBILITY_ID, "Delivering to Add Address")
    add_new_address = (AppiumBy.ACCESSIBILITY_ID, "Add new")
    address = (AppiumBy.XPATH, "//android.widget.ImageView | //XCUIElementTypeImage")
    home_address = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Home')]")
    work_address = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Work')]")
    qhira_address = (AppiumBy.XPATH, "//*[contains(@content-desc, 'qhira')]")
    dora_address = (AppiumBy.XPATH, "//*[contains(@content-desc, 'dora')]")
    food_category = (AppiumBy.ACCESSIBILITY_ID, "Food")
    deliver_to_text = (AppiumBy.ACCESSIBILITY_ID, "Deliver to")
    outside_address_box = (AppiumBy.CLASS_NAME, "android.widget.FrameLayout")
    missing_items_input_field = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    missing_items_submit_button = (AppiumBy.ACCESSIBILITY_ID, "SUBMIT")


class CategoryPageSelectors:
    canned_foods_sub_category = (AppiumBy.ACCESSIBILITY_ID, "Canned Foods")
    first_item_plus_icon = (AppiumBy.XPATH, "(//android.view.View[contains(@content-desc,'IQD')])[1]/android.widget.ImageView[2]")
    second_item_plus_icon = (
        AppiumBy.XPATH, "(//android.view.View[contains(@content-desc,'IQD')])[2]/android.widget.ImageView[2]")
    bath_supplies_category = (AppiumBy.ACCESSIBILITY_ID, "Bath Supplies_1")
    landessa_product = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Landessa')]/android.widget.ImageView")


class ProductsPageSelectors:
    product_item = (AppiumBy.XPATH, "//*[@*[contains(.,'IQD')]]/android.widget.ImageView")
    sauce_filter = (AppiumBy.ACCESSIBILITY_ID, "Sauce")


class ProductItemPageSelectors:
    description_title = (AppiumBy.ACCESSIBILITY_ID, "Description")
    file = open("./plus_icon.png", "rb")
    add_icon = (AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8'))
    file.close()
    add_icon_2 = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                  ".FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View"
                                  "/android.view.View/android.view.View[1]/android.view.View[8]")
    view_basket_button = (AppiumBy.ACCESSIBILITY_ID, "View Basket")
    basket_total_2500 = (AppiumBy.XPATH, "//android.view.View[@content-desc='2,500 IQD']")
    basket_total_5000 = (AppiumBy.XPATH, "//android.view.View[@content-desc='5,000 IQD']")
    basket_qt_1 = (AppiumBy.XPATH, "//android.view.View[@content-desc='1']")
    basket_qt_2 = (AppiumBy.XPATH, "//android.view.View[@content-desc='2']")
    star_icon = (AppiumBy.XPATH, "//android.widget.ImageView/following-sibling::android.view.View")
    item_price = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Lovita Choco')]/following-sibling::android.view.View")
    cart_limit_warning_message = (AppiumBy.ACCESSIBILITY_ID, "IQD 1,990 to reach min order")
    similar_products_title = (AppiumBy.ACCESSIBILITY_ID, "Similar products")
    yahia_item_02 = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'yahia_item_02')]")
    yahia_item_03 = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'yahia_item_03')]")
    yahia_item_04 = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'yahia_item_04')]")
    file = open("./share_icon.png", "rb")
    share_icon = (AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8'))
    file.close()


class CartPageSelectors:
    cart_page_title = (AppiumBy.ACCESSIBILITY_ID, "Cart")
    cart_item = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'IQD')]")
    clear_button = (AppiumBy.ACCESSIBILITY_ID, "Clear Cart")
    checkout_button = (AppiumBy.ACCESSIBILITY_ID, "CHECKOUT")
    empty_cart_text = (AppiumBy.ACCESSIBILITY_ID, "Empty Shelf")
    file = open("./plus_icon.png", "rb")
    plus_icon = (AppiumBy.IMAGE, base64.b64encode(file.read()).decode('utf-8'))
    file.close()
    minus_icon_first_element = (
        AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'IQD')][1]/android.view.View[1]")
    total_amount = (
        AppiumBy.XPATH, "//android.view.View[@content-desc='Total Amount']/following-sibling::android.view.View")
    sub_total = (AppiumBy.XPATH, "//android.view.View[@content-desc='Sub-Total']/following-sibling::android.view.View")
    delivery_charge = (
        AppiumBy.XPATH, "//android.view.View[@content-desc='Delivery Charges']/following-sibling::android.view.View")
    total_amount_after_promo_code = (
        AppiumBy.XPATH,
        "//android.view.View[@content-desc='Total Amount']/following-sibling::android.view.View/following-sibling::android.view.View")
    promo_code = (AppiumBy.XPATH, "(//android.widget.ImageView)[3]")
    apply_promo = (AppiumBy.ACCESSIBILITY_ID, "Apply")
    remove_promo = (AppiumBy.ACCESSIBILITY_ID, "Remove")
    missing_items_message = (
        AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Missing items in your Cart')]")
    view_replace_button = (AppiumBy.ACCESSIBILITY_ID, "View & Replace")
    subtotal_amount_before_promo_code = (
    AppiumBy.XPATH, "//android.view.View[@content-desc='Sub-Total']/following-sibling::android.view.View")
    subtotal_amount_after_promo_code = (AppiumBy.XPATH,
                                        "//android.view.View[@content-desc='Sub-Total']/following-sibling::android.view.View/following-sibling::android.view.View")


class ReplaceMissingItems:
    remove_btn = (AppiumBy.ACCESSIBILITY_ID, "Remove")
    replace_and_update_btn = (AppiumBy.XPATH, "//android.widget.Button[contains(@content-desc,'replace & update')]")
    confirmation_message = (
        AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'Missing Items Are Updated Successfully')]")
    new_total_amount = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'IQD 19,000')]")
    place_order_btn = (AppiumBy.ACCESSIBILITY_ID, "Place Order")
    yahia_item_04_plus_icon = (
        AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'5,000')]/child::android.view.View")


class CheckOutPageSelectors:
    checkout_page_title = (AppiumBy.ACCESSIBILITY_ID, "Checkout")
    place_order_button = (AppiumBy.ACCESSIBILITY_ID, "PLACE ORDER")
    confirmation_popup = (AppiumBy.ACCESSIBILITY_ID, "Order Created Successfully")
    done_button = (AppiumBy.ACCESSIBILITY_ID, "Done")
    work_address = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'Work')]")
    selected_address_work = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Work')]")
    selected_address_home = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Home')]")
    schedule_button = (AppiumBy.IMAGE, base64.b64encode(open("./schedule_btn.png", "rb").read()).decode('utf-8'))
    schedule_order_button = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Schedule Order']")
    schedule_day = lambda day: (AppiumBy.XPATH, f"//android.view.View[contains(@content-desc,'{day}')]")


class ReceiptPageSelectors:
    order_id = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Order ID')]")
    cancel_button = (AppiumBy.IMAGE, base64.b64encode(open("./cancel_order.jpg", "rb").read()).decode('utf-8'))
    deliver_section_title = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'Deliver')]")
    order_status_section_title = (AppiumBy.ACCESSIBILITY_ID, "Order Status")
    order_summary_title = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Order Summary')]")
    shopping_bag_title = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'Shopping Bag')]")
    confirm_cancel_button = (AppiumBy.ACCESSIBILITY_ID, "CONFIRM")
    done_button = (AppiumBy.ACCESSIBILITY_ID, "DONE")
    cancelled_label = (AppiumBy.ACCESSIBILITY_ID, "Canceled")
    scheduled_label = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Scheduled')]")
    reason_list = (AppiumBy.ACCESSIBILITY_ID, "Select cancellation reason")
    cancel_reason = (AppiumBy.ACCESSIBILITY_ID, "I regret the purchase")
    modify_order = (AppiumBy.ACCESSIBILITY_ID, "Modify Order")
    update_order = (AppiumBy.ACCESSIBILITY_ID, "Update order")
    suggest_missing_items_button = (AppiumBy.ACCESSIBILITY_ID, "Press Here")
    text_of_missing_items = (
    AppiumBy.ACCESSIBILITY_ID, "Inform us about the products you need that you did not find in Taza")


class OrderHistoryPageSelectors:
    history_page_title = (AppiumBy.ACCESSIBILITY_ID, "Order History")
    current_order_item = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Order placed')]")
    past_tab = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Past')]")
    past_order_item = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Canceled')]")
    scheduled_tab = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Scheduled')]")
    scheduled_order_item = (
        AppiumBy.XPATH,
        "//android.view.View[contains(@content-desc,'Order ID') and contains(@content-desc,'Scheduled')]")
    placed_order_with_certain_id = lambda orderID: (
        AppiumBy.XPATH, f"//android.view.View[contains(@content-desc,'{orderID}')]")


class LanguagePageSelectors:
    arabic = (AppiumBy.ACCESSIBILITY_ID, "Arabic")
    english = (AppiumBy.ACCESSIBILITY_ID, "الإنجليزية")
    page_title_arabic = (AppiumBy.ACCESSIBILITY_ID, "اللغة")
    page_title_english = (AppiumBy.ACCESSIBILITY_ID, "Language")
    back_button = (AppiumBy.CLASS_NAME, "android.widget.ImageView")


class AccountDetailsPageSelectors:
    delete_Account_button = (AppiumBy.ACCESSIBILITY_ID, "Delete account")
    confirm_delete_button = (AppiumBy.ACCESSIBILITY_ID, "Delete")
    OK_button = (AppiumBy.ACCESSIBILITY_ID, "OK")
    confirmation_message = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'Sorry to see you go')]")
    first_name = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
    last_name = (AppiumBy.XPATH, "(//android.widget.EditText)[2]")
    account_save = (AppiumBy.ACCESSIBILITY_ID, "Save")
    account_back = (AppiumBy.XPATH, "//android.view.View[1]")
    account_email = (AppiumBy.XPATH, "(//android.widget.EditText)[4]")
    account_phone = (AppiumBy.XPATH, "//android.view.View[6] | //XCUIElementTypeOther[5]")


class SignUpPageSelectors:
    first_name_input_field = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
    last_name_input_field = (AppiumBy.XPATH, "(//android.widget.EditText)[2]")
    mobile_no_input_field = (AppiumBy.XPATH, "(//android.widget.EditText)[3]")
    password_input_field = (AppiumBy.XPATH, "(//android.widget.EditText)[4]")
    next_button = (AppiumBy.ACCESSIBILITY_ID, "NEXT")


class SavedAddressesPageSelectors:
    saved_addresses_page_title = (AppiumBy.XPATH, "//android.view.View[@content-desc='Saved Addresses' and "
                                                  "@clickable='false']")
    add_icon = (AppiumBy.CLASS_NAME, "android.widget.Button")
    address_nickname = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'Home')]")
    address_updated_nickname = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,"
                                                "'edit_home')]")
    update_button = (AppiumBy.ACCESSIBILITY_ID, "Update")
    delete_button = (AppiumBy.ACCESSIBILITY_ID, "Delete")
    yes_button = (AppiumBy.ACCESSIBILITY_ID, "Yes")
    not_found_text = (AppiumBy.ACCESSIBILITY_ID, "Not found")
    dots_icon = (AppiumBy.IMAGE, base64.b64encode(open("./dots.jpg", "rb").read()).decode('utf-8'))


class NewAddressPageSelectors:
    next_button = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'NEXT')]")
    allow_gps_button = (AppiumBy.XPATH, "//android.widget.Button[@text='While using the app']")
    not_available_button = (AppiumBy.ACCESSIBILITY_ID, "Not available")
    search_input_field_inactive = (AppiumBy.XPATH, "//android.view.View[@content-desc='Use current "
                                                   "location']/preceding-sibling::android.view.View")
    search_input_field_active = (AppiumBy.XPATH, "//android.widget.EditText")
    baghdad_mall_search_result = (AppiumBy.XPATH, "//android.view.View[contains(@content-desc,'Kindi Street')]")
    deliver_to_button = (AppiumBy.ACCESSIBILITY_ID, "Deliver here")
    nick_name = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
    neighbourhood = (AppiumBy.XPATH,
                     "(//android.widget.Button[@content-desc = 'Baghdad']/following-sibling::android.widget.EditText)[1]")
    district = (AppiumBy.XPATH,
                "(//android.widget.Button[@content-desc = 'Baghdad']/following-sibling::android.widget.EditText)[2]")
    save_address = (AppiumBy.ACCESSIBILITY_ID, "SAVE ADDRESS")
    update_button = (AppiumBy.ACCESSIBILITY_ID, "Update")


class FavoritesPageSelectors:
    item_description_selector = "//android.view.View[contains(@content-desc,'{}')]".format(DataSets.product_item_en)
    item_description = (AppiumBy.XPATH, item_description_selector)
    star_icon = (AppiumBy.IMAGE, base64.b64encode(open("./blue_star.png", "rb").read()).decode('utf-8'))
    no_favorites_text = (AppiumBy.XPATH, "//android.widget.ImageView[contains(@content-desc,'No favourites yet')]")
