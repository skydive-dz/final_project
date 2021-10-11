from .base_page import BasePage
from .locators import BasketLocators
from .locators import BasePageLocators

class BasketPage(BasePage):

	def should_be_basket_button(self):
		assert self.is_element_present(*BasePageLocators.BASKET_BUTTON), 'Busket button is not presented!'

	def check_product_in_basket(self):
		assert self.is_not_element_present(*BasketLocators.EMPTY_BASKET), 'The busket is not empty!'

	def message_about_empty_basket(self):
		assert self.is_element_present(*BasketLocators.MESSAGE_ABOUT_EMPTY_BASKET), "The message not present!"
		