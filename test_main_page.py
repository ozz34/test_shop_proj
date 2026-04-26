from .pages.product_page import ProductPage
import pytest

LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        product_page = ProductPage(browser, LINK)
        product_page.open()
        product_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        product_page = ProductPage(browser, LINK)
        product_page.open()
        product_page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, LINK)
    product_page.open()
    product_page.open_bucket()
    product_page.check_empty_bucket_message()

