from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def should_be_button_active(self):
        assert self.is_element_present(*ProductPageLocators.BUCKET_BUTTON), "Add bucket button is not presented"

    def check_product_param(self):
        product_name = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME)
        ).text
        product_price = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_PRICE)
        ).text
        return (product_name, product_price)

    def add_product_to_basket(self):
        add_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.BUCKET_BUTTON)
        )
        add_button.click()

    def check_success_add_to_basket(self, product):
        get_text = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_ADDED_MESSAGE)
        ).text
        need_text = f"{product[0]} has been added to your basket."
        assert need_text == get_text, f"Должно быть сообщение {need_text} , но в выводе сообщение {get_text}"
        print(f"{need_text}")

        assert WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.PRICE_MESSAGE)
        ).text.__contains__(f"{product[1]}"), f"Стоимость в корзине не соответствует"
        print(f"Стоимость в корзине {product[1]}")

