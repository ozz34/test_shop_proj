from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def should_be_button_active(self):
        assert self.is_element_present(*ProductPageLocators.BUCKET_BUTTON), "Add bucket button is not presented"

    def add_product_to_basket(self):
        add_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.BUCKET_BUTTON)
        )
        add_button.click()

    def check_success_add_to_basket(self):
        get_text = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_ADDED_MESSAGE)
        ).text
        need_text = "The shellcoder's handbook has been added to your basket."
        assert need_text == get_text, f"Должно быть сообщение {need_text} , но в выводе сообщение {get_text}"
        print(f"{need_text}")

        assert WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.PRICE_MESSAGE)
        ).text.__contains__("£9.99"), f"Стоимость в корзине не соответствует"
        print(f"Стоимость в корзине £9.99")

