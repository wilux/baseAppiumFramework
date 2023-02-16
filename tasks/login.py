from steps import login, home
from steps import start, validate_device


def with_data(driver, data):
    start.tap_tengo_cuenta(driver)
    login.enter_with_credentials(driver, data.get("user"), data.get("password"))
    login.no_finger_print(driver)
    validate_device.add_device(driver, data.get("user"))
    home.deslizar_para_continuar(driver)
