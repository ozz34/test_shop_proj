from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_BUCKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_ADDED_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[@class = 'price_color']")
    PRICE_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket total is now')]/strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUCKET_LINK = (By.XPATH, "//span[@class = 'btn-group']")
    BUCKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div[id = 'content_inner'] p")
