from actions import find


def text(driver, element):
    """
    This function received an element and then
    return text from it.
    """
    e = find.locator(driver, element)
    return driver.find_element(e[0], e[1]).text


def by_text(driver, value):
    """
    This function receive a text, and then it try to find a valid element,
    finally text from it.
    """
    e = find.locator_by_text(driver, value)
    return driver.find_element(e[0], e[1]).text

