import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os
from dotenv import load_dotenv
from utils import attach
from appium import webdriver


username = os.getenv('LOGIN')
access_key = os.getenv('PASSWORD')

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": username,
            "accessKey": access_key
        }
    })

    browser.config.driver = webdriver.Remote(
        "http://hub.browserstack.com/wd/hub",
        options=options
    )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
