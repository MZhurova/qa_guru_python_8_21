import allure
import allure_commons
import pytest
import config

from appium.options.android import UiAutomator2Options
from selene import browser, support
from appium import webdriver
from utils import attach


@pytest.fixture(scope='function')
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "12.0",
        "deviceName": "Samsung Galaxy S22 Ultra",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Android tests",
            "buildName": "browserstack-wikipedia-build",
            "sessionName": "BStack wikipedia_test",

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

    attach.screenshot()
    attach.page_source_xml()
    session_id = browser.driver.session_id
    browser.quit()
    attach.bstack_video(session_id)