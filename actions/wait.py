from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions import find


def visibility_of_element_located(driver, element, time):
    """
     This function receive an element,
     find the locator and them wait for it be visible.
     """
    e = find.locator(driver, element)
    try:
        WebDriverWait(driver, time).until(EC.visibility_of_element_located((e[0], e[1])))
        return True
    except TimeoutException as ex:
        print(ex)
        return False


def visibility_of_element_located_by_text(driver, text, time):
    """
     This function receive an element,
     find the locator by text and them wait for it be visible
     """
    e = find.locator_by_text(driver, text)
    try:
        WebDriverWait(driver, time).until(EC.visibility_of_element_located((e[0], e[1])))
        return True
    except TimeoutException as ex:
        print(ex)
        return False


def element_to_be_clickable(driver, element, time):
    """
     This function receive an element,
     find the locator and them wait for it be clickable.
     """
    e = find.locator(driver, element)
    try:
        WebDriverWait(driver, time).until(EC.element_to_be_clickable((e[0], e[1])))
        return True
    except TimeoutException as ex:
        print(ex)
        return False


def text_to_be_present_in_element(driver, element, text, time):
    """
     This function receive an element,
     wait for text_to_be_present_in_element
     """
    e = find.locator(driver, element)
    try:
        WebDriverWait(driver, time).until(EC.text_to_be_present_in_element_value((e[0], e[1]), text))
        return True
    except TimeoutException as ex:
        print(ex)
        return False


def element_by_text_and_be_clickable(driver, text, time):
    """
     This function receive an element,
     find the locator by text and them wait for it be clickable.
     """
    e = find.locator_by_text(driver, text)
    try:
        WebDriverWait(driver, time).until(EC.element_to_be_clickable((e[0], e[1])))
        return True
    except TimeoutException as ex:
        print(ex)
        return False
