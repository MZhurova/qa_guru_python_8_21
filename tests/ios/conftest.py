import allure
import allure_commons
import pytest
import config

from appium.options.ios import XCUITestOptions
from selene import browser, support
from appium import webdriver
from utils import attach


@pytest.fixture(scope='function')
def ios_mobile_management():
    options = XCUITestOptions().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "ios",
        "platformVersion": "17",
        "deviceName": "iPhone 15 Pro Max",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Ios tests",
            "buildName": "browserstack-simple-app-build",
            "sessionName": "BStack Simple app test",

            # Set your access credentials
            "userName": config.username,
            "accessKey": config.access_key
        }
    })

    with allure.step('setup app session'):
        browser.config.driver = webdriver.Remote(
            config.remote_browser_url,
            options=options
        )

    browser.config.timeout = 10.0

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()