import allure
import allure_commons
import pytest
import config

from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support
from appium import webdriver
from utils import allure_attach


@pytest.fixture(scope='function')
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "13.0",
        "deviceName": "Samsung Galaxy S23 Ultra",

        # Set URL of the application under test
        "app": "bs://sample.app",
        # "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",

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

    allure_attach.screenshot()

    allure_attach.page_source_xml()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    allure_attach.bstack_video(session_id)


@pytest.fixture(scope='function')
def ios_mobile_management():
    options = XCUITestOptions().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "ios",
        "platformVersion": "16",
        "deviceName": "iPhone 14 Pro Max",

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

    allure_attach.screenshot()

    allure_attach.page_source_xml()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    allure_attach.bstack_video(session_id)
