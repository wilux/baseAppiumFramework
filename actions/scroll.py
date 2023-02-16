import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


def to(driver, x):
    """
    This function allows you to scroll the screen up or down a pre-set number of pixels.
    Parameters: up or down
    """
    if x == 'up':
        a = 1000
        b = 200
    elif x == "down":
        a = 200
        b = 1000
    else:
        assert False, "Invalid scroll option, just can be up or down"
    os = driver.capabilities.get('platformName')
    if os == "Android":
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1000, a)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(2)
        actions.w3c_actions.pointer_action.move_to_location(1000, b)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(2)
    else:
        driver.execute_script('mobile: scroll', {'direction': x})
        time.sleep(2)

