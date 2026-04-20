from selenium.webdriver.common.by import By

class ProductPageLocators():
    BUCKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_ADDED_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    PRICE_MESSAGE = (By.XPATH, "//strong[text() = '£9.99']")

