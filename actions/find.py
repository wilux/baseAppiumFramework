from appium.webdriver.common.appiumby import AppiumBy


def locator(driver, element):
    """
    This function verify the platform to use to find
    the correct locator.
    """
    os = driver.capabilities.get('platformName')
    if os == "Android":
        e = element['android']
    elif os == "iOS":
        e = element['ios']
    else:
        assert False, "The platform on which you are running this test is not compatible with the framework."
    return e[0], e[1]


def locator_by_text(driver, text):
    """
    This function verify the platform to use to find
    the correct locator from a text y return webelement
    """
    os = driver.capabilities.get('platformName')
    if os == "Android":
        return (AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textContains("' + text + '")')
    elif os == "iOS":
        return (AppiumBy.IOS_PREDICATE,
                'label == "' + text + '" OR name == "' + text + '" OR ''value == "' + text + '"')
    else:
        assert False, "The platform on which you are running this test is not compatible with the framework."
