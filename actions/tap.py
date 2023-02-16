from selenium.webdriver import ActionChains
from actions import find


def on(driver, element):
    """
    This function received an element and then
    tap/click over it.
    """
    e = find.locator(driver, element)
    driver.find_element(e[0], e[1]).click()


def by_action(driver, element):
    """
    This function received an element and then
    tap/click over it using ActionsChains.
    """
    e = find.locator(driver, element)
    element = driver.find_element(e[0], e[1])
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.click(element)
    actions.perform()


def by_action_with_text(driver, text):
    """
    This function received an element and then
    tap/click over it using ActionsChains.
    """
    e = find.locator_by_text(driver, text)
    element = driver.find_element(e[0], e[1])
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.click(element)
    actions.perform()


def by_text(driver, text):
    """
    This function receive a text, and then it try to find a valid element,
    finally tap/click over the found element.
    """
    e = find.locator_by_text(driver, text)
    driver.find_element(e[0], e[1]).click()

