from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search(android_mobile_management):
    # with step('Tap on the skip button'):
    #     browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')).click()
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_search_google(android_mobile_management):
    # with step('Tap on the skip button'):
    #     browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')).click()
    with step('Type search "Google"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Google')

    with step('Verify content found "Google"'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Google'))