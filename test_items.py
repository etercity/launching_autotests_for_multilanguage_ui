import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_getting_page(browser):
    browser.get(link)
    time.sleep(30)


