from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):

	def should_be_product_page_link(self):
		assert "?promo=newYear" == self.browser.current_url, 'This is not a product page!'

	def add_to_basket(self):
		self.should_be_name()
		self.should_be_price()
		self.should_be_add_button()

		button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
		self.solve_quiz_and_get_code()
		self.should_be_success_message()

	def should_be_add_button(self):
		assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), 'The button add to busket not found!'

	def should_be_name(self):
		assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Product name not found!'

	def should_be_price(self):
		assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), 'Product price not found!'
		
	def should_be_correct_name(self):
		self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		self.product_name_into_busket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_INTO_BASKET).text
		assert product_name == product_name_into_busket, 'Invalid product name!'

	def should_be_correct_price(self):
		self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		self.product_price_into_busket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_INTO_BASKET).text
		assert product_price == product_price_into_busket, 'Invalid product price!'


	def should_be_success_message(self):
		assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE), 'Should be a succsess message!'

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

	def success_message_should_disappear(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should"

