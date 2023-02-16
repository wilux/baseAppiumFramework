from selenium.webdriver import ActionChains
from actions import find


def on(driver, element, text):
    """
    This function received an element and then
    send keys over it.
    """
    e = find.locator(driver, element)
    el = driver.find_element(e[0], e[1])
    el.click()
    # el.clear()
    el.send_keys(text)


def with_action(driver, element, text):
    """
    This function received an element and then
    send keys over it using ActionsChains
    """
    if driver.capabilities.get('platformName') == "iOS":
        on(driver, element, text)
    else:
        e = find.locator(driver, element)
        text_view = driver.find_element(e[0], e[1])
        text_view.click()
        actions = ActionChains(driver)
        actions.send_keys_to_element(text_view, text)
        actions.perform()


def with_action_and_by_text(driver, text, value):
    """
    This function received an element and then
    send keys over it using ActionsChains
    """
    e = find.locator_by_text(driver, text)
    text_view = driver.find_element(e[0], e[1])
    text_view.click()
    actions = ActionChains(driver)
    actions.send_keys_to_element(text_view, value)
    actions.perform()


def by_text(driver, text, value):
    """
    This function received a text locator find the element and then
    send keys over it.
    """
    e = find.locator_by_text(driver, text)
    el = driver.find_element(e[0], e[1])
    el.clear()
    el.send_keys(value)

