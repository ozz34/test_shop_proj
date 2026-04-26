from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_button_bucket_active(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUCKET_BUTTON), "Add bucket button is not presented"

    def check_product_param(self):
        product_name = self.is_element_visible(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.is_element_visible(*ProductPageLocators.PRODUCT_PRICE).text
        return (product_name, product_price)

    def add_product_to_basket(self):
        add_button = self.is_element_clickable(*ProductPageLocators.ADD_BUCKET_BUTTON)
        add_button.click()

    def check_success_add_to_basket(self, product):
        get_text = self.is_element_visible(*ProductPageLocators.SUCCESS_ADDED_MESSAGE).text
        need_text = f"{product[0]} has been added to your basket."
        assert need_text == get_text, f"Должно быть сообщение {need_text} , но в выводе сообщение {get_text}"
        print(f"{need_text}")

        assert self.is_element_visible(*ProductPageLocators.PRICE_MESSAGE).text.__contains__(f"{product[1]}"), \
            f"Стоимость в корзине не соответствует"
        print(f"Стоимость в корзине {product[1]}")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADDED_MESSAGE), \
            "Success message should be disappeared, but not"