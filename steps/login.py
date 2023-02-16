from selenium.webdriver.common.by import By
from actions import wait, tap, send_keys
from locators.login import LoginLocators


def enter_with_credentials(driver, user, password):
    if wait.element_to_be_clickable(driver, LoginLocators.email_input, 10):
        if driver.capabilities.get('platformName') == "iOS":
            tap.on(driver, LoginLocators.email_input)
            try:
                driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="Borrar texto"]').click()
            except:
                pass
        send_keys.on(driver, LoginLocators.email_input, user)
        send_keys.on(driver, LoginLocators.password_input, password)
        tap.on(driver, LoginLocators.continue_btn)
    else:
        assert False


def no_finger_print(driver):
    try:
        tap.on(driver, LoginLocators.fingerprint_no_btn)
    except:
        pass

