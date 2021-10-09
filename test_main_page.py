import time
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    time.sleep(3)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()