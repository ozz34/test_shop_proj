from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(browser, link)
    product_page.open()
    product = product_page.check_product_param()
    product_page.should_be_button_active()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_success_add_to_basket(product)










