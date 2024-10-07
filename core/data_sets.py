import string
import random
import time


class DataSets:
    product_item_en = "Lovita Choco"
    product_item_ar = "لوفيتا"
    product_item_en_1 = "yahia_item_01"  # 10 IQD
    promo_code_1 = "yahia1234"
    promo_code_2 = "yahia2345"
    cart_object_1 = [{
        "item_code": "CN-CB-ROS-0000003",
        "qty": "1"}]
    cart_object_2 = [{
        "item_code": "B-TAG-0000001",
        "qty": "4"},
        {"item_code": "B-brand_code-0000002",
         "qty": "4"}]

    """
    the following are the data for registering new user
    """
    register_first_name = "yahia"
    register_last_name = "soliman"
    register_phone = ""
    register_password = "1234"

    """ 
    the following are data of customer that has Work address and Home address
    """
    phone = "7807113335"
    password = "1234"
    otp_key_codes = [8, 8, 8, 8]
    new_password = "4444"
    first_name = "yahia2"
    last_name = "soliman"
    email = "yahia@gmail.com"

    # the following account for schedule order
    phoneSchedule = "7807113336"

    """ 
     the following are data of customer that has address of Qahira darkstore
      and address of Dora darkstore
     """
    phone_darkStore = "7807113375"
    lovita_qhira_price = "500 IQD"  # price list two
    lovita_dora_price = "2,500 IQD"  # price list one

    """
    the following are the data used for creating new address
    """
    search_value = "Baghdad Mall"
    nickname_home = "Home"
    nickname_work = "Work"
    neighbourhood_value = "test_neighbourhood"
    district_value = "test_district"
    new_nickname = "edit_home"

    """
    the following are credentials for user to be used for updating account information
    with random name and email
    """
    phone_for_account_update = "7897341742"
    password_for_account_update = "1234"

    """
    generate random name to use for updating account information
    """

    @staticmethod
    def generate_random_name():
        result = ''.join(random.choices(string.ascii_lowercase +
                                        string.digits, k=7))
        return result

    """
    generate random email to use for updating account information
    """

    @staticmethod
    def generate_random_email():
        result = ''.join(random.choices(string.ascii_lowercase +
                                        string.digits, k=7))
        return result + "@mail.com"

    """
    generate random phone number
    """

    @staticmethod
    def generate_random_phone_number():
        x = str(time.time())
        y = x[-5:]
        return "78973" + y
