import os
from appium import webdriver
from pytest_html_reporter import attach
import pytest

REPORTS = "reports/"

if not os.path.exists(REPORTS):
    os.makedirs(REPORTS)


def pytest_addoption(parser):
    parser.addoption(
        "--device",
        action="store",
        default="android",
        help="select device",
        choices=("android", "ios")
    )


@pytest.fixture(scope="session", autouse=True)
def device(request):
    return request.config.getoption("--device")


# Share the appium driver between functions
@pytest.fixture
def driver(device):
    # Driver configurations
    command_executor = 'http://localhost:4723/wd/hub'
    print("Preparing device: " + device)
    if device == 'android':
        desired_capabilities = dict(
            platformName="Android",
            appPackage="",
            appActivity="",
            automationName="UiAutomator2",
            unicodeKeyboard=True,
            resetKeyboard=True,
            isHeadless=False)
    else:
        desired_capabilities = dict(
            bundleId="",
            deviceName="iPhone 14 pro max",
            udid="C0E6EA73-910F-4FE2-A7CA-6FBDCC2CD08A",
            automationName="XCUITest",
            platformName="iOS",
            noReset=False)
    driver = webdriver.Remote(command_executor, desired_capabilities)
    driver.implicitly_wait(5)
    driver.update_settings({'waitForIdleTimeout': 100})
    yield driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    if report.when == 'call' or report.failed:
        feature_request = item.funcargs["request"]
        driver = feature_request.getfixturevalue("driver")
        attach(data=driver.get_screenshot_as_png())

