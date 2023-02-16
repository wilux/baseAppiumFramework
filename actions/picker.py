import time
from appium.webdriver.common.appiumby import AppiumBy
from actions import tap


def on(driver, element, text):
    """
    This function pick over a picker element
    and select by text sent.
    """
    tap.on(driver, element)
    el = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypePickerWheel')
    el.send_keys(text)
    try:
        tap.by_text(driver, "OK")
    except:
        pass


def scroll_type_on(driver, element, text):
    """
    This function pick over a select with scroll element
    and select by text sent.
    """
    tap.on(driver, element)
    time.sleep(5)
    tap.by_text(driver, text)
    time.sleep(5)

