import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_exist(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    # time.sleep(10)
    button = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert button, "button is missing"




