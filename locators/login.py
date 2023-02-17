from appium.webdriver.common.appiumby import AppiumBy


class LoginLocators(object):
    """
    This class gather all locators from
    a screen in the dictionary way key-value to
    set android and/or ios locator
    """

    email_input = {
        "android": [AppiumBy.ID, ''],
        "ios": [AppiumBy.IOS_CLASS_CHAIN, '']
    }
