from appium.webdriver.common.appiumby import AppiumBy


def hidde_keyboard(driver):
    """
    This function hidde keyboard
    on iOS
    """
    os = driver.capabilities.get('platformName')
    if os == "iOS":
        try:
            el = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Done"`]')
            el.click()
        except:
            pass


def permission_ok(driver):
    """
    This function tap on OK button
    on iOS when show popup the permissions
    """
    os = driver.capabilities.get('platformName')
    if os == "iOS":
        try:
            el = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "OK"`]')
            el.click()
        except:
            pass


def permission_one_time(driver):
    """
    This function tap on Permitir una vez button
    on iOS when show popup the permissions
    """
    os = driver.capabilities.get('platformName')
    if os == "iOS":
        try:
            el = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Permitir una '
                                                                    'vez"`]')
            el.click()
        except:
            pass


def permission_contacts(driver):
    """
    This function enable contacts permission
    on iOS
    """
    os = driver.capabilities.get('platformName')
    if os == "iOS":
        try:
            el = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[`value == "0"`][2]')
            el.click()
            driver.back()
            driver.back()
        except:
            pass


def permission_photos(driver):
    """
    This function tap on Permitir una vez button
    on iOS when show popup the permissions
    """
    os = driver.capabilities.get('platformName')
    if os == "iOS":
        try:
            el = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Permitir '
                                                                    'acceso a todas las fotos"`]')
            el.click()
        except:
            pass
