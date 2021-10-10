from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest

product_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
promo_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
main_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, promo_link)
    page.open()
    page.add_to_basket()
    page.should_be_name()
    page.should_be_price()
    page.should_be_success_message()

def test_user_can_add_product_to_basket_from_main_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_to_basket()
    page.should_be_name()
    page.should_be_price()
    page.should_be_success_message()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfile),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_name()
    page.should_be_price()
    page.should_be_success_message()


