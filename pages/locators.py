from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMALE = (By.CSS_SELECTOR, '[name = "registration-email"]')
    REGISTER_PSWD = (By.CSS_SELECTOR, '[name = "registration-password1"]')
    REGISTER_CONFIRM_PSWD = (By.CSS_SELECTOR, '[name = "registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')

class ProductPageLocators():
    ADD_TO_BUSKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main p.price_color')
    PRODUCT_NAME_INTO_BASKET = (By.CSS_SELECTOR, "#messages div:first-child div.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")