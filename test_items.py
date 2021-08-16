import time


def test_user_should_see_basket_button(browser):
    time.sleep(10)
    button = len(browser.find_elements_by_css_selector("button.btn.btn-lg"))
    assert button > 0, 'not found'